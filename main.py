import multiprocessing
import sys
from PySide2.QtWidgets import QApplication
from PySide2 import QtGui

import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl

try:
    import pyi_splash
except ModuleNotFoundError:
    pass
from main_window import Ui_MainWindow, QMainWindow
import conf


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

        # Callbacks:
        self.combo_applicator.activated.connect(self.refresh)
        self.combo_bevel.activated.connect(self.refresh)
        self.dosis_edit.textChanged.connect(self.refresh)
        self.radio1.toggled.connect(self.refresh)
        self.radio2.toggled.connect(self.refresh)
        self.radio3.toggled.connect(self.refresh)
        self.radio4.toggled.connect(self.refresh)
        self.calcular.clicked.connect(self.calculate_UM)

        self.calcular.setEnabled(False)
        self.img1 = pg.ImageItem()
        self.data_cross = None

        self.pref = conf.PREF  # Reference Pressure
        self.label_pref.setText(str(self.pref))

        # Pyqtgraph image_____________________________________
        self.p1 = self.graphWidget1.addPlot(colspan=1, title="Crossline")
        self.p1.addItem(self.img1)

        self.p2 = self.graphWidget2.addPlot(colspan=1, title="Inline")
        self.p3 = self.graphWidget3.addPlot(colspan=1, title="Isodosis del 90% en zmax")

        self.extent_cross = [1, 1]
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

        print(self.npzfile)
        if (
                (a_idx >= 0) and
                (b_idx >= 0) and
                (self.dosis_edit.text() != '') and
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
            self.calcular.setEnabled(True)
            self.plot_distribs()
        else:
            self.npzfile = ''
            self.dose_distrib = None
            self.calcular.setEnabled(False)
        self.output_label.setText('')
        self.UM_label.setText('')

    def plot_distribs(self):
        results = self.dose_distrib
        D = results['Dose']
        Xbin, Ybin, Zbin = D.shape
        x_scale = np.unique(results['X'])
        x_start = x_scale[0]
        x_end = x_scale[-1]
        y_scale = np.unique(results['Y'])
        y_start = y_scale[0]
        y_end = y_scale[-1]
        z_scale = np.unique(results['Z'])
        z_start = z_scale[0]
        z_end = z_scale[-1]
        d_x = x_scale[1] - x_scale[0]
        d_y = y_scale[1] - y_scale[0]
        d_z = z_scale[1] - z_scale[0]
        self.d_x = d_x
        self.d_y = d_y
        self.d_z = d_z
        self.extent_cross = [-d_x / 2 + x_start, x_end + d_x / 2, z_start - d_z / 2, z_end + d_z / 2]
        print(f'extent crossline: {self.extent_cross}')
        self.extent3D = [x_start, x_end, y_start, y_end, z_start, z_end]
        print(f'3D extent: {self.extent3D}')

        self.p1.clear()

        self.img1 = pg.ImageItem()
        self.p1.addItem(self.img1)
        plane_idx = int(round(np.median(range(Ybin))))
        # TODO: interpolate at x = 0 or y = 0, create mesh?
        self.data_cross = np.rot90(D[:, plane_idx, :])
        # Interpolate to get max in clinical axis
        self.img1.setImage(self.data_cross)
        self.p1.addColorBar(self.img1, colorMap='turbo')

        tr = QtGui.QTransform()  # prepare ImageItem transformation:
        tr.translate(self.extent_cross[0], self.extent_cross[3])
        tr.scale((self.extent_cross[1] - self.extent_cross[0]) / Xbin,
                 (self.extent_cross[3] - self.extent_cross[2]) / Zbin)  # scale horizontal and vertical axes
        print(f'x_start: {x_start}')
        print(f'x_end: {x_end}')
        print(f'y_start: {y_start}')
        print(f'y_end: {y_end}')

        self.p1.addItem(pg.GridItem())
        self.p1.getViewBox().invertY(True)
        self.p1.getViewBox().setAspectLocked(lock=True, ratio=1)
        self.p1.getAxis('bottom').setLabel('cm')

        levels = np.linspace(self.data_cross.min(), self.data_cross.max(), 10)
        for level in levels:
            iso_curve = pg.IsocurveItem(level=level, pen='k')
            iso_curve.setData(self.data_cross)
            self.p1.addItem(iso_curve)
            iso_curve.setTransform(tr)
        self.img1.setTransform(tr)
        self.p1.autoRange()

        # 3D
        self.openGLWidget.clear()
        self.openGLWidget.setCameraPosition(distance=20)
        g = gl.GLGridItem()
        self.openGLWidget.addItem(g)
        levels = [1.05, 0.9, 0.2]
        reds = [1.0, 0.8, 0]
        greens = [0.0, 0.4, 0]
        alphas = [0.2, 0.3, 255]
        for idx, level in enumerate(levels):
            self.create_3D_isodose(level=level, red=reds[idx], green=greens[idx], alpha=alphas[idx])
        # 3D Cylinder
        applicator = int(self.combo_applicator.currentText())
        md = gl.MeshData.cylinder(rows=10, cols=20, radius=[applicator / 2, applicator / 2], length=5.0)
        colors = np.zeros((md.faceCount(), 4), dtype=float)
        colors[:, 1] = 0.1  # 0.2
        colors[:, 3] = 100  # 0.2
        colors[:, 2] = np.linspace(0, 1, colors.shape[0])
        md.setFaceColors(colors)
        m = gl.GLMeshItem(meshdata=md, smooth=True, shader='balloon')
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
        self.dose = float(self.dosis_edit.text())
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
