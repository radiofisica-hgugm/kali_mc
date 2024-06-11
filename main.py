import multiprocessing
import sys
from PySide2.QtWidgets import QApplication, QFileDialog
from PySide2 import QtGui

import numpy as np
from scipy.interpolate import RegularGridInterpolator
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import pyqtgraph.exporters
import datetime
import tempfile, os

try:
    import pyi_splash
except ModuleNotFoundError:
    pass
from main_window import Ui_MainWindow, QMainWindow
import conf
from report_utils import create_pdf

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.initial_title = self.windowTitle()
        self.energies = [6, 8, 10, 12]
        self.npzfile = ''
        self.dose_distrib = None
        self.dose = 0
        self.cGy_UM = 0
        self.UM = 0
        self.clinical_max = 0
        self.z_clinical_max = 0
        self.x_scale = 0
        self.y_scale = 0
        self.z_scale = 0
        self.Xbin = 0
        self.Ybin = 0
        self.Zbin = 0
        self.levels = np.array([10, 30, 50, 70, 80, 90, 100, 110])
        self.grid_factor = 0.5  # Finer grid

        # Callbacks:
        self.combo_applicator.activated.connect(self.refresh)
        self.combo_bevel.activated.connect(self.refresh)
        self.DoseEdit.textChanged.connect(self.refresh)
        self.radio1.toggled.connect(self.refresh)
        self.radio2.toggled.connect(self.refresh)
        self.radio3.toggled.connect(self.refresh)
        self.radio4.toggled.connect(self.refresh)
        self.phoy_edit.textChanged.connect(self.refresh)
        self.calcular.clicked.connect(self.calculate_UM)
        self.pushreport.clicked.connect(self.generate_report)

        self.calcular.setEnabled(False)
        self.img1 = pg.ImageItem()
        self.img2 = pg.ImageItem()
        self.data_cross = None
        self.data_in = None
        self.colorbar_cross = None
        self.colorbar_in = None

        self.pref = conf.PREF  # Reference Pressure
        self.label_pref.setText(str(self.pref))

        # Pyqtgraph image_____________________________________
        self.p1 = self.graphWidget1.addPlot(colspan=1, title="Crossline")
        self.p1.addItem(self.img1)

        self.p2 = self.graphWidget2.addPlot(colspan=1, title="Inline")
        self.p2.addItem(self.img2)
        self.p3 = self.graphWidget3.addPlot(colspan=1, title="Isodosis del 90% en zmax")

        self.extent_cross = [1, 1]
        self.extent_in = [1, 1]
        self.extent3D = [1, 1, 1]
        self.d_x = 0.0
        self.d_y = 0.0
        self.d_z = 0.0

        g = gl.GLGridItem()
        self.openGLWidget.addItem(g)

        self.graphWidget1.setBackground('w')
        self.graphWidget2.setBackground('w')
        self.graphWidget3.setBackground('w')
        self.openGLWidget.opts['bgcolor'] = (0.3, 0.3, 0.3, 1)

        # Interpret image data as row-major instead of col-major
        # Otherwise, image shows rotated 90ยบ
        pg.setConfigOptions(imageAxisOrder='row-major')

    def find_checked_radiobutton(self):
        """ find the checked radiobutton, returns energy index """
        radiobuttons = [self.radio1, self.radio2, self.radio3, self.radio4]
        checked_radiobutton_idx = -1
        for e_idx, rb in enumerate(radiobuttons):
            if rb.isChecked():
                checked_radiobutton_idx = e_idx
        return checked_radiobutton_idx

    def refresh(self):
        a_idx = self.combo_applicator.currentIndex() - 1  # applicator index
        applicator = self.combo_applicator.currentText()
        b_idx = self.combo_bevel.currentIndex() - 1  # bevel index
        bevel = self.combo_bevel.currentText()
        pressure = self.phoy_edit.text()

        # print(self.npzfile)
        if (
                (a_idx >= 0) and
                (b_idx >= 0) and
                (self.DoseEdit.text() != '') and
                (self.radio1.isChecked() or
                 self.radio2.isChecked() or
                 self.radio3.isChecked() or
                 self.radio4.isChecked()
                )
        ):
            energy_idx = self.find_checked_radiobutton()
            self.npzfile = rf'data\sim\C{applicator}\B{bevel}\C{applicator}B{bevel}_{self.energies[energy_idx]}MeV.npz'
            results = np.load(self.npzfile, allow_pickle=True)
            self.dose_distrib = results['SpatialDoseDistrib'][()]
            R90_array = np.load(rf'data/R90_C{applicator}.npz')['R90'][:, b_idx]  # load R90 data
            self.label_6MeV.setText(f'{R90_array[0]:.1f}')
            self.label_8MeV.setText(f'{R90_array[1]:.1f}')
            self.label_10MeV.setText(f'{R90_array[2]:.1f}')
            self.label_12MeV.setText(f'{R90_array[3]:.1f}')

            if pressure != '':
                self.calcular.setEnabled(True)
            self.plot_distribs()
        else:
            self.npzfile = ''
            self.dose_distrib = None
            self.calcular.setEnabled(False)
        self.output_label.setText('')
        self.UM_label.setText('')
        self.label_linac_dose.setText('')
        self.label_linac_energy.setText('')
        self.label_linac_applicator.setText('')

    def plot_distribs(self):
        results = self.dose_distrib
        D = results['Dose']
        self.Xbin, self.Ybin, self.Zbin = D.shape
        self.x_scale = np.unique(results['X'])
        x_start = self.x_scale[0]
        x_end = self.x_scale[-1]
        self.y_scale = np.unique(results['Y'])
        y_start = self.y_scale[0]
        y_end = self.y_scale[-1]
        self.z_scale = np.unique(results['Z'])
        z_start = self.z_scale[0]
        z_end = self.z_scale[-1]
        d_x = self.x_scale[1] - self.x_scale[0]
        d_y = self.y_scale[1] - self.y_scale[0]
        d_z = self.z_scale[1] - self.z_scale[0]
        self.d_x = d_x
        self.d_y = d_y
        self.d_z = d_z
        self.extent_cross = [-d_x / 2 + x_start, x_end + d_x / 2, z_start - d_z / 2, z_end + d_z / 2]
        self.extent_in = [-d_y / 2 + y_start, y_end + d_y / 2, z_start - d_z / 2, z_end + d_z / 2]
        # print(f'extent crossline: {self.extent_cross}')
        self.extent3D = [x_start, x_end, y_start, y_end, z_start, z_end]
        # print(f'3D extent: {self.extent3D}')

        # Create the interpolator
        interpolator = RegularGridInterpolator((self.x_scale, self.y_scale, self.z_scale), D)


        # Interpolate to get max in clinical axis  ____________________________________________________________________
        x_val = 0
        y_val = 0
        z_vals = np.linspace(np.min(self.z_scale), np.max(self.z_scale))
        points = np.array([[x_val, y_val, z] for z in z_vals])
        depth_dose = interpolator(points)
        self.clinical_max = np.max(depth_dose)
        self.z_clinical_max = z_vals[np.argmax(depth_dose)]

        # plot cross plane
        self.plot_crossplane(interpolator)

        # plot inline plane
        self.plot_inplane(interpolator)

        # 3D
        self.openGLWidget.clear()
        self.openGLWidget.setCameraPosition(distance=20, azimuth=-55, elevation=15)

        g = gl.GLGridItem()
        self.openGLWidget.addItem(g)
        levels = [1.05, 0.9, 0.2]
        reds = [1.0, 0.8, 0]
        greens = [0.0, 0.4, 0]
        alphas = [0.2, 0.3, 255]
        for idx, level in enumerate(levels):
            self.create_3D_isodose(level=level, red=reds[idx], green=greens[idx], alpha=alphas[idx])

        # 3D Cylinder
        self.add_inclined_cylinder()

    def plot_crossplane(self, interpolator):
        plot_relative = True

        self.p1.clear()
        self.img1 = pg.ImageItem()
        self.p1.addItem(self.img1)

        # Define the points on the y=0 plane for interpolation
        x_vals = np.linspace(self.x_scale[0], self.x_scale[-1], int(len(self.x_scale) * (1 / self.grid_factor)))
        y_val = 0
        z_vals = np.linspace(self.z_scale[0], self.z_scale[-1], int(len(self.z_scale) * (1 / self.grid_factor)))
        X_plane, Z_plane = np.meshgrid(x_vals, z_vals, indexing='ij')

        # Create the grid points for the y=0 plane
        points_plane = np.vstack([X_plane.ravel(), y_val * np.ones_like(X_plane.ravel()), Z_plane.ravel()]).T

        # Interpolate the data on the y=0 plane
        D_plane = interpolator(points_plane).reshape(X_plane.shape)
        self.data_cross = np.rot90(D_plane)
        data = self.data_cross
        self.p1.addItem(pg.GridItem())
        self.p1.getViewBox().invertY(True)
        self.p1.getViewBox().setAspectLocked(lock=True, ratio=1)
        self.p1.getAxis('bottom').setLabel('cm')
        extent = self.extent_cross

        if plot_relative:
            data = data / self.clinical_max * 100
            levels = self.levels
        else:
            levels = self.levels * self.clinical_max / 100
        self.img1.setImage(data)

        # Colorbar
        if self.colorbar_cross:
            self.colorbar_cross.setParentItem(None)
            self.colorbar_cross = None

        self.colorbar_cross = pg.ColorBarItem(values=(data.min(), data.max()), colorMap='turbo')
        self.colorbar_cross.setImageItem(self.img1, insert_in=self.p1)

        tr = QtGui.QTransform()  # prepare ImageItem transformation:
        tr.translate(extent[0], extent[3])
        tr.scale((extent[1] - extent[0]) / len(x_vals),
                 (extent[3] - extent[2]) / len(z_vals))  # scale horizontal and vertical axes

        for level in levels:
            iso_curve = pg.IsocurveItem(level=level, pen='k')
            iso_curve.setData(data)
            self.p1.addItem(iso_curve)
            iso_curve.setParentItem(self.img1)
            # Find a position to place the text
            pos = self.find_text_position(data, level)
            if pos is not None:
                text = pg.TextItem(f'{level:.2f}', anchor=(0.5, 0.5))
                text.setPos(pos[0], pos[1])
                self.p1.addItem(text)
                text.setParentItem(self.img1)

        self.img1.setTransform(tr)
        self.p1.autoRange()

    def plot_inplane(self, interpolator):
        plot_relative = True

        self.p2.clear()
        self.img2 = pg.ImageItem()
        self.p2.addItem(self.img2)

        # Define the points on the y=0 plane for interpolation
        x_vals = 0
        y_vals = np.linspace(self.y_scale[0], self.y_scale[-1], int(len(self.y_scale) * (1 / self.grid_factor)))
        z_vals = np.linspace(self.z_scale[0], self.z_scale[-1], int(len(self.z_scale) * (1 / self.grid_factor)))
        Y_plane, Z_plane = np.meshgrid(y_vals, z_vals, indexing='ij')

        # Create the grid points for the y=0 plane
        points_plane = np.vstack([x_vals * np.ones_like(Y_plane.ravel()), Y_plane.ravel(), Z_plane.ravel()]).T

        # Interpolate the data on the y=0 plane
        D_plane = interpolator(points_plane).reshape(Y_plane.shape)
        self.data_in = np.rot90(D_plane)
        self.p2.addItem(pg.GridItem())
        self.p2.getViewBox().invertY(True)
        self.p2.getViewBox().setAspectLocked(lock=True, ratio=1)
        self.p2.getAxis('bottom').setLabel('cm')

        if plot_relative:
            data = self.data_in / self.clinical_max * 100
            levels = self.levels
        else:
            data = self.data_in
            levels = self.levels * self.clinical_max / 100
        self.img2.setImage(data)

        # Colorbar
        if self.colorbar_in:
            self.colorbar_in.setParentItem(None)
            self.colorbar_in = None

        self.colorbar_in = pg.ColorBarItem(values=(data.min(), data.max()), colorMap='turbo')
        self.colorbar_in.setImageItem(self.img2, insert_in=self.p2)

        tr = QtGui.QTransform()  # prepare ImageItem transformation:
        extent = self.extent_in
        tr.translate(extent[0], extent[3])
        tr.scale((extent[1] - extent[0]) / len(y_vals),
                 (extent[3] - extent[2]) / len(z_vals))  # scale horizontal and vertical axes

        for level in levels:
            iso_curve = pg.IsocurveItem(level=level, pen='k')
            iso_curve.setData(data)
            self.p2.addItem(iso_curve)
            iso_curve.setParentItem(self.img2)
            # Find a position to place the text
            pos = self.find_text_position(data, level)
            if pos is not None:
                text = pg.TextItem(f'{level:.2f}', anchor=(0.5, 0.5))
                text.setPos(pos[0], pos[1])
                self.p2.addItem(text)
                text.setParentItem(self.img2)

        self.img2.setTransform(tr)
        self.p2.autoRange()



    def find_text_position(self, data, level):
        """
        Find a suitable position to place the text label for a given iso level.
        """
        mask = data >= level
        y, x = np.where(mask)
        if len(x) > 0 and len(y) > 0:
            # Use the center of the largest cluster of points as the position
            x_center = np.min(x) + (np.max(x) - np.min(x)) * 0.75
            y_center = np.max(y)
            return x_center, y_center
        return None

    def add_inclined_cylinder(self):
        # Define the cylinder parameters
        height = 5
        sectors = 50  # Number of sectors for the circular base
        angle = float(self.combo_bevel.currentText())  # Inclination angle in degrees
        inclination_radians = np.radians(-angle)
        radius_y = float(self.combo_applicator.currentText()) / 2  # Scale y semi-minor axis
        radius_x = radius_y / np.cos(inclination_radians)  # Scale y semi-major axis

        # Create the cylinder mesh data
        verts = []
        faces = []

        # Create vertices for the base and top of the cylinder
        for i in range(sectors):
            theta = 2 * np.pi * i / sectors
            y = radius_y * np.cos(theta)
            x = radius_x * np.sin(theta)
            z_bottom = 0
            z_top = height * np.cos(inclination_radians)
            x_top = x + height * np.sin(inclination_radians)

            verts.append((x, y, z_bottom))
            verts.append((x_top, y, z_top))

        for i in range(sectors):
            j = (i + 1) % sectors
            faces.append((i * 2, j * 2, i * 2 + 1))
            faces.append((j * 2, j * 2 + 1, i * 2 + 1))

            # Bottom and top faces
        for i in range(sectors - 2):
            faces.append((0, (i + 1) * 2, (i + 2) * 2))
            faces.append((1, (i + 2) * 2 + 1, (i + 1) * 2 + 1))

        verts = np.array(verts)
        faces = np.array(faces)

        # Create the mesh item
        meshdata = gl.MeshData(vertexes=verts, faces=faces)
        colors = np.zeros((meshdata.faceCount(), 4), dtype=float)
        colors[:, 1] = 0.1  # 0.2
        colors[:, 3] = 100  # 0.2
        colors[:, 2] = 0 # 0 -> green, 1-> blue
        meshdata.setFaceColors(colors)
        m = gl.GLMeshItem(meshdata=meshdata, smooth=True, shader='balloon')
        m.setGLOptions('additive')

        self.openGLWidget.addItem(m)

    def create_3D_isodose(self, level, red, green, alpha):
        D = self.dose_distrib['Dose']
        Xbin, Ybin, Zbin = D.shape
        verts, faces = pg.isosurface(D, D.max() * level)
        md = gl.MeshData(vertexes=verts, faces=faces)
        colors = np.ones((md.faceCount(), 4), dtype=float) * red
        colors[:, 1] = green  # 0.2
        colors[:, 3] = alpha  # 0.2
        colors[:, 2] = np.linspace(0, 1, colors.shape[0])
        md.setFaceColors(colors)
        m = gl.GLMeshItem(meshdata=md, smooth=True, shader='balloon')
        m.setGLOptions('additive')
        self.openGLWidget.addItem(m)
        m.translate(self.extent3D[0] + self.d_x / 2, self.extent3D[2] + self.d_y / 2, self.extent3D[4] + self.d_z / 2)
        m.scale((self.extent3D[1] - self.extent3D[0]) / Xbin, (self.extent3D[3] - self.extent3D[2]) / Ybin,
                (self.extent3D[5] - self.extent3D[4]) / Zbin)

    def calculate_UM(self):
        # Retrieve data from gui:
        self.dose = float(self.DoseEdit.text())
        applicator = self.combo_applicator.currentText()
        b_idx = self.combo_bevel.currentIndex() - 1  # bevel index
        energy_idx = self.find_checked_radiobutton()
        p_today = float(self.phoy_edit.text())  # Pressure correction

        # Load output from file and calculate
        OFs = np.load(rf'data\OF_C{applicator}.npz', allow_pickle=True)['arr_0']
        self.cGy_UM = OFs[b_idx, energy_idx]
        self.output_label.setText(f'{self.cGy_UM:.3f}')
        prescription_isodose = 90
        self.UM = int(np.round(self.dose/self.cGy_UM/(prescription_isodose/100)/self.pref*p_today))
        self.UM_label.setText(str(self.UM))
        self.label_linac_dose.setText(str(self.UM))
        self.label_linac_energy.setText(f'{self.energies[energy_idx]} MeV')
        self.label_linac_applicator.setText(f'{int(applicator)*10} mm')

    def generate_report(self):
        data_dict = self.create_data_dict()
        pdf_path = os.path.join(conf.pdf_path, f"{data_dict['Date']} {data_dict['Name']} {data_dict['Surname']}.pdf")
        name = QFileDialog.getSaveFileName(self, 'Guardar informe pdf',
                                           pdf_path,
                                           "Archivos pdf (*.pdf)")
        if name[0] != "":
            print('Generating report ..........')
            self.p1.autoRange()
            self.p2.autoRange()
            with tempfile.TemporaryDirectory() as tempdir:
                exporter = pg.exporters.ImageExporter(self.p1)
                file_cross = os.path.join(tempdir, 'cross.png')
                exporter.export(file_cross)

                exporter = pg.exporters.ImageExporter(self.p2)
                file_in = os.path.join(tempdir, 'in.png')
                exporter.export(file_in)

                file_3D = os.path.join(tempdir,'3D.png')
                self.openGLWidget.grabFramebuffer().save(file_3D)

                create_pdf(name[0], file_cross, file_in, file_3D, data_dict)
                print('Report saved')
        else:
            print('Report cancelled')

    def create_data_dict(self):
        energy_idx = self.find_checked_radiobutton()

        data_dict = {
            'Name': self.NameEdit.text(),
            'Surname': self.SurnameEdit.text(),
            'ID': self.IDEdit.text(),
            'Site': self.SiteEdit.text(),
            'Physicist': self.PhysicistEdit.text(),
            'Oncologist': self.OncologistEdit.text(),
            'TERt': self.TechnologistEdit.text(),

            'Applicator': self.combo_applicator.currentText(),
            'Bevel': self.combo_bevel.currentText(),
            'Dose': self.DoseEdit.text(),

            'Energy': self.energies[energy_idx],
            'Output': self.output_label.text(),
            'UM': self.UM_label.text(),

            'Pitch': self.PitchEdit.text(),
            'Roll': self.RollEdit.text(),
            'Vertical': self.VerticalEdit.text(),

            'IORT_number': self.IORTnumberEdit.text(),
            'Date': datetime.date.today(),

            'Comments': self.CommentsEdit.toPlainText()
        }
        return data_dict


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    try:

        pyi_splash.update_text("Kali MC starting...")
        pyi_splash.close()

    except NameError:
        pass
    sys.exit(app.exec_())
