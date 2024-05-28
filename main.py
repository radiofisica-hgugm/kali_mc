import multiprocessing
import os
import sys
from PySide2.QtWidgets import QApplication
from PySide2 import QtGui
import threading

import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl
#from PIL import Image
try:
    import pyi_splash
except:
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

        # Callbacks:
        self.combo_applicator.activated.connect(self.refresh)
        self.combo_bevel.activated.connect(self.refresh)
        self.dosis_edit.textChanged.connect(self.refresh)
        self.radio1.toggled.connect(self.refresh)
        self.radio2.toggled.connect(self.refresh)
        self.radio3.toggled.connect(self.refresh)
        self.radio4.toggled.connect(self.refresh)

        self.calcular.setEnabled(False)
        self.img1 = pg.ImageItem()

        self.pref = conf.PREF # Reference Pressure
        self.label_pref.setText(str(self.pref))

        # Pyqtgraph image_____________________________________
        self.p1 = self.graphWidget1.addPlot(colspan=1, title="Crossline")
        self.p1.addItem(img_item := self.img1)
        #self.p1.addColorBar(img_item, colorMap='viridis', values=(0, 1))
        self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.img1)
        self.h1 = self.graphWidget1.addItem(self.hist)


        self.p2 = self.graphWidget2.addPlot(colspan=1, title="Inline")
        self.p3 = self.graphWidget3.addPlot(colspan=1, title="Isodosis del 90% en zmax")

        g = gl.GLGridItem()
        self.openGLWidget.addItem(g)


        # FAKE DATA
        x = np.random.normal(size=1000)
        y = np.random.normal(size=1000)
        z = np.random.normal(size=1000)

        pts = np.vstack([x, y, z]).transpose()
        scatter = gl.GLScatterPlotItem(pos=pts, color=(1, 1, 1, 1), size=0.1)
        self.openGLWidget.addItem(scatter)



        self.graphWidget1.setBackground('w')
        self.graphWidget2.setBackground('w')
        self.graphWidget3.setBackground('w')
        # self.openGLWidget.opts['bgcolor'] = (0.5, 0.5, 0.5, 1) #GREY
        self.openGLWidget.opts['bgcolor'] = (0.3, 0.3, 0.3, 1)

        # Interpret image data as row-major instead of col-major
        # Otherwise, image shows rotated 90ยบ
        pg.setConfigOptions(imageAxisOrder='row-major')

    def find_checked_radiobutton(self):
        """ find the checked radiobutton, returns energy index """
        radiobuttons = [self.radio1, self.radio2, self.radio3, self.radio4]
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

    def change_gradient(self, gradient_name):
        # Define gradient presets
        gradient_presets = {
            'viridis': pg.colormap.get('viridis'),
            'plasma': pg.colormap.get('plasma'),
            'inferno': pg.colormap.get('inferno'),
            'magma': pg.colormap.get('magma'),
            'cividis': pg.colormap.get('cividis'),
            'turbo': pg.colormap.get('turbo')
        }

        # Apply the selected gradient
        if gradient_name in gradient_presets:
            colormap = gradient_presets[gradient_name]
            lut = colormap.getLookupTable()
            self.img1.setLookupTable(lut)
            #self.img1.setLevels([0, 1])  # Normalize the data to [0, 1]

    def plot_distribs(self):
        results = self.dose_distrib
        D = results['Dose']
        # S = results['Sigma']
        X = results['X']
        Y = results['Z']
        Xbin, Ybin, Zbin = D.shape
        x_scale = np.unique(X)
        x_start = x_scale[0]
        x_end = x_scale[-1]
        y_scale = np.unique(Y)
        y_start = y_scale[0]
        y_end = y_scale[-1]
        d_x = x_scale[1] - x_scale[0]
        d_y = y_scale[1] - y_scale[0]
        extent = [-d_x + x_start, x_end + d_x, y_start - d_y, y_end + d_y]

        self.p1.clear()
        self.img1 = pg.ImageItem()
        self.p1.addItem(self.img1)
        plane_idx = int(round(np.median(range(Ybin))))
        # TODO: interpolate at x = 0 or y = 0, create mesh?
        self.data = np.rot90(D[:, plane_idx, :])
        self.img1.setImage(self.data)
        # self.hist = pg.HistogramLUTItem()
        self.hist.setImageItem(self.img1)
        # self.h1 = self.graphWidget1.addItem(self.hist)
        # self.reset_tools()
        tr = QtGui.QTransform()  # prepare ImageItem transformation:
        tr.translate(x_start - d_x, y_end + d_y/2)
        tr.scale((extent[1] - extent[0])/len(x_scale), (y_end - y_start)/len(y_scale))  # scale horizontal and vertical axes
        print(f'x_start: {x_start}')
        print(f'x_end: {x_end}')
        print(f'y_start: {y_start}')
        print(f'y_end: {y_end}')

        self.p1.addItem(pg.GridItem())
        self.p1.getViewBox().invertY(True)
        self.p1.getViewBox().setAspectLocked(lock=True, ratio=1)
        self.change_gradient('turbo')
        levels = np.linspace(self.data.min(), self.data.max(), 10)
        for level in levels:
            iso_curve = pg.IsocurveItem(level=level, pen='k')
            iso_curve.setData(self.data)
            self.p1.addItem(iso_curve)
            iso_curve.setTransform(tr)
        self.img1.setTransform(tr)
        self.p1.autoRange()

        # 3D
        alpha = 0.3
        self.openGLWidget.clear()
        self.openGLWidget.setCameraPosition(distance=20)
        g = gl.GLGridItem()
        self.openGLWidget.addItem(g)
        v = gl.GLVolumeItem(D)
        verts, faces = pg.isosurface(D, D.max() *0.9)
        md = gl.MeshData(vertexes=verts, faces=faces)
        colors = np.ones((md.faceCount(), 4), dtype=float)
        colors[:, 1] = 0.0  # 0.2
        colors[:, 3] = alpha # 0.2
        colors[:, 2] = np.linspace(0, 1, colors.shape[0])
        md.setFaceColors(colors)
        m2 = gl.GLMeshItem(meshdata=md, smooth=True, shader='balloon')
        m2.setGLOptions('additive')

        self.openGLWidget.addItem(m2)
        # m2.translate(-D.shape[0]/2, -D.shape[1]/2, -D.shape[2]+1)
        m2.scale((extent[1] - extent[0]) / len(x_scale), (extent[1] - extent[0]) / len(x_scale), (y_end - y_start) / len(y_scale))
        # m2.translate(x_start - d_x, x_start - d_x, y_start + d_y / 2)
        m2.translate(x_start - d_x/2, x_start - d_x/2, y_start -d_y/2)

        verts, faces = pg.isosurface(D, D.max() * 0.2)
        md = gl.MeshData(vertexes=verts, faces=faces)
        colors = np.zeros((md.faceCount(), 4), dtype=float) #BLUE
        colors[:, 1] = 0.0  # 0.2
        colors[:, 3] = alpha  # 0.2
        colors[:, 2] = np.linspace(0, 1, colors.shape[0])
        md.setFaceColors(colors)
        m3 = gl.GLMeshItem(meshdata=md, smooth=True, shader='balloon')
        m3.setGLOptions('additive')

        self.openGLWidget.addItem(m3)
        # m3.translate(-D.shape[0] / 2, -D.shape[1] / 2, -D.shape[2] + 1)
        m3.scale((extent[1] - extent[0]) / len(x_scale), (extent[1] - extent[0]) / len(x_scale),
                 (y_end - y_start) / len(y_scale))
        m3.translate(x_start - d_x/2, x_start - d_x/2, y_start -d_y/2)





        # fig, [(ax0, ax1), (ax2, ax3)] = plt.subplots(
        #     2, 2, sharey=True, figsize=(10, 9))
        # fig.suptitle('Tally Spatial Dose Distribution')
        #
        # # XZ Plane
        # plane_idx = int(round(np.median(range(Ybin))))
        # p0 = ax0.imshow(np.rot90(D[:, plane_idx, :]), extent=extent)
        # CS = ax0.contour(X[:, plane_idx, :], Y[:, plane_idx, :],
        #                  D[:, plane_idx, :], levels=5, colors=('k',), linewidths=(0.5,))
        # if isolevels:
        #     ax0.clabel(CS, fmt='%2.1f', colors='w', fontsize=8)
        # fig.colorbar(p0, ax=ax0)
        # ax0.set_title('XZ Dose (eV/(g*hist))')
        # ax0.set_xlabel('x (cm)')
        # ax0.set_ylabel('z (cm)')
        #
        # p1 = ax1.imshow(np.rot90(S[:, plane_idx, :]), extent=extent)
        # fig.colorbar(p1, ax=ax1)
        # ax1.set_title('XZ Sigma (%)')
        # ax1.set_xlabel('x (cm)')
        #
        # # YZ Plane
        # X = results['Y']
        # x_scale = np.unique(X)
        # x_start = x_scale[0]
        # x_end = x_scale[-1]
        # y_scale = np.unique(Y)
        # y_start = y_scale[0]
        # y_end = y_scale[-1]
        # d_x = x_scale[1] - x_scale[0]
        # d_y = y_scale[1] - y_scale[0]
        # extent = [-d_x + x_start, x_end + d_x, y_start - d_y, y_end + d_y]
        # plane_idx = int(round(np.median(range(Xbin))))
        # p2 = ax2.imshow(np.rot90(D[plane_idx, :, :]), extent=extent)
        # CS2 = ax2.contour(X[plane_idx, :, :], Y[plane_idx, :, :],
        #                   D[plane_idx, :, :], levels=5, colors=('k',), linewidths=(0.5,))
        # if isolevels:
        #     ax2.clabel(CS2, fmt='%2.1f', colors='w', fontsize=8)
        # fig.colorbar(p2, ax=ax2)
        # ax2.set_title('YZ Dosis (eV/(g*hist))')
        # ax2.set_xlabel('y (cm)')
        # ax2.set_ylabel('z (cm)')
        #
        # p3 = ax3.imshow(np.rot90(S[plane_idx, :, :]), extent=extent)
        # fig.colorbar(p3, ax=ax3)
        # ax3.set_title('YZ Sigma (%)')
        # ax3.set_xlabel('y (cm)')
        # plt.show()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    try:

        pyi_splash.update_text("Kali MC starting...")
        pyi_splash.close()

    except:
        pass
    sys.exit(app.exec_())