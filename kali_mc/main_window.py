# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QMainWindow,
    QMenuBar,
    QPlainTextEdit,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from pyqtgraph import GraphicsLayoutWidget
from pyqtgraph.opengl import GLViewWidget
import main_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1468, 886)
        icon = QIcon()
        icon.addFile(
            ":/icons/res/kali_ico.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.horizontalLayout.setContentsMargins(-1, 4, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(11, -1, -1, 5)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        font = QFont()
        font.setFamilies(["Lucida Sans"])
        font.setPointSize(15)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setMinimumSize(QSize(230, 80))
        font1 = QFont()
        font1.setFamilies(["Lucida Sans"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setKerning(False)
        self.groupBox.setFont(font1)
        self.formLayout_4 = QFormLayout(self.groupBox)
        self.formLayout_4.setObjectName("formLayout_4")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_3.setContentsMargins(-1, -1, 15, -1)
        self.combo_applicator = QComboBox(self.groupBox)
        self.combo_applicator.addItem("")
        self.combo_applicator.addItem("")
        self.combo_applicator.addItem("")
        self.combo_applicator.addItem("")
        self.combo_applicator.addItem("")
        self.combo_applicator.addItem("")
        self.combo_applicator.addItem("")
        self.combo_applicator.addItem("")
        self.combo_applicator.addItem("")
        self.combo_applicator.addItem("")
        self.combo_applicator.setObjectName("combo_applicator")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.combo_applicator)

        self.combo_bevel = QComboBox(self.groupBox)
        self.combo_bevel.addItem("")
        self.combo_bevel.addItem("")
        self.combo_bevel.addItem("")
        self.combo_bevel.addItem("")
        self.combo_bevel.addItem("")
        self.combo_bevel.setObjectName("combo_bevel")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.combo_bevel)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMaximumSize(QSize(16, 16))
        self.label_9.setPixmap(QPixmap(":/icons/res/angle-icon-blue.svg"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies(["Lucida Sans"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setKerning(False)
        self.label_3.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.formLayout_3.setLayout(1, QFormLayout.LabelRole, self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMaximumSize(QSize(16, 16))
        self.label_12.setPixmap(QPixmap(":/icons/res/cylinder.svg"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_12)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.formLayout_3.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout_5)

        self.formLayout_4.setLayout(1, QFormLayout.SpanningRole, self.formLayout_3)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        font3 = QFont()
        font3.setFamilies(["Lucida Sans"])
        font3.setPointSize(12)
        self.groupBox_2.setFont(font3)
        self.formLayoutWidget_2 = QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 20, 231, 61))
        self.formLayout_5 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_5.setObjectName("formLayout_5")
        self.formLayout_5.setContentsMargins(0, 0, 15, 0)
        self.label_4 = QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font2)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.DoseEdit = QLineEdit(self.formLayoutWidget_2)
        self.DoseEdit.setObjectName("DoseEdit")
        self.DoseEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.DoseEdit)

        self.label_5 = QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font2)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.depth_edit = QLineEdit(self.formLayoutWidget_2)
        self.depth_edit.setObjectName("depth_edit")
        self.depth_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.depth_edit)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setFont(font3)
        self.gridLayoutWidget = QWidget(self.groupBox_3)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 271, 182))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_12MeV = QLabel(self.gridLayoutWidget)
        self.label_12MeV.setObjectName("label_12MeV")
        font4 = QFont()
        font4.setFamilies(["Lucida Sans"])
        font4.setPointSize(11)
        self.label_12MeV.setFont(font4)
        self.label_12MeV.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_12MeV, 4, 1, 1, 1)

        self.label_rescale_ico_12 = QLabel(self.gridLayoutWidget)
        self.label_rescale_ico_12.setObjectName("label_rescale_ico_12")
        self.label_rescale_ico_12.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.label_rescale_ico_12.sizePolicy().hasHeightForWidth()
        )
        self.label_rescale_ico_12.setSizePolicy(sizePolicy)
        self.label_rescale_ico_12.setMaximumSize(QSize(16, 16))
        self.label_rescale_ico_12.setScaledContents(True)

        self.gridLayout.addWidget(self.label_rescale_ico_12, 4, 2, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        font5 = QFont()
        font5.setFamilies(["Lucida Sans"])
        font5.setPointSize(11)
        font5.setBold(True)
        self.label_11.setFont(font5)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_8MeV = QLabel(self.gridLayoutWidget)
        self.label_8MeV.setObjectName("label_8MeV")
        self.label_8MeV.setFont(font4)
        self.label_8MeV.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_8MeV, 2, 1, 1, 1)

        self.label_rescale_ico_6 = QLabel(self.gridLayoutWidget)
        self.label_rescale_ico_6.setObjectName("label_rescale_ico_6")
        self.label_rescale_ico_6.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.label_rescale_ico_6.sizePolicy().hasHeightForWidth()
        )
        self.label_rescale_ico_6.setSizePolicy(sizePolicy)
        self.label_rescale_ico_6.setMaximumSize(QSize(16, 16))
        self.label_rescale_ico_6.setScaledContents(True)

        self.gridLayout.addWidget(self.label_rescale_ico_6, 1, 2, 1, 1)

        self.label_rescale_ico_10 = QLabel(self.gridLayoutWidget)
        self.label_rescale_ico_10.setObjectName("label_rescale_ico_10")
        self.label_rescale_ico_10.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.label_rescale_ico_10.sizePolicy().hasHeightForWidth()
        )
        self.label_rescale_ico_10.setSizePolicy(sizePolicy)
        self.label_rescale_ico_10.setMaximumSize(QSize(16, 16))
        self.label_rescale_ico_10.setScaledContents(True)

        self.gridLayout.addWidget(self.label_rescale_ico_10, 3, 2, 1, 1)

        self.radio4 = QRadioButton(self.gridLayoutWidget)
        self.radio4.setObjectName("radio4")
        self.radio4.setFont(font4)

        self.gridLayout.addWidget(self.radio4, 4, 0, 1, 1)

        self.radio1 = QRadioButton(self.gridLayoutWidget)
        self.radio1.setObjectName("radio1")
        self.radio1.setFont(font4)

        self.gridLayout.addWidget(self.radio1, 1, 0, 1, 1)

        self.radio3 = QRadioButton(self.gridLayoutWidget)
        self.radio3.setObjectName("radio3")
        self.radio3.setFont(font4)

        self.gridLayout.addWidget(self.radio3, 3, 0, 1, 1)

        self.label_6MeV = QLabel(self.gridLayoutWidget)
        self.label_6MeV.setObjectName("label_6MeV")
        self.label_6MeV.setFont(font4)
        self.label_6MeV.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_6MeV, 1, 1, 1, 1)

        self.label_10MeV = QLabel(self.gridLayoutWidget)
        self.label_10MeV.setObjectName("label_10MeV")
        self.label_10MeV.setFont(font4)
        self.label_10MeV.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_10MeV, 3, 1, 1, 1)

        self.radio2 = QRadioButton(self.gridLayoutWidget)
        self.radio2.setObjectName("radio2")
        self.radio2.setFont(font4)

        self.gridLayout.addWidget(self.radio2, 2, 0, 1, 1)

        self.label_rescale_ico_8 = QLabel(self.gridLayoutWidget)
        self.label_rescale_ico_8.setObjectName("label_rescale_ico_8")
        self.label_rescale_ico_8.setEnabled(True)
        sizePolicy.setHeightForWidth(
            self.label_rescale_ico_8.sizePolicy().hasHeightForWidth()
        )
        self.label_rescale_ico_8.setSizePolicy(sizePolicy)
        self.label_rescale_ico_8.setMaximumSize(QSize(16, 16))
        self.label_rescale_ico_8.setScaledContents(True)

        self.gridLayout.addWidget(self.label_rescale_ico_8, 2, 2, 1, 1)

        self.label_rescale_f_8 = QLabel(self.gridLayoutWidget)
        self.label_rescale_f_8.setObjectName("label_rescale_f_8")
        font6 = QFont()
        font6.setFamilies(["Lucida Sans"])
        font6.setPointSize(8)
        font6.setBold(False)
        self.label_rescale_f_8.setFont(font6)
        self.label_rescale_f_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_rescale_f_8, 2, 3, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget)
        self.label_35.setObjectName("label_35")
        font7 = QFont()
        font7.setFamilies(["Lucida Sans"])
        font7.setPointSize(9)
        font7.setBold(True)
        self.label_35.setFont(font7)
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_35, 0, 3, 1, 1)

        self.label_rescale_f_6 = QLabel(self.gridLayoutWidget)
        self.label_rescale_f_6.setObjectName("label_rescale_f_6")
        self.label_rescale_f_6.setFont(font6)
        self.label_rescale_f_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_rescale_f_6, 1, 3, 1, 1)

        self.label_rescale_f_10 = QLabel(self.gridLayoutWidget)
        self.label_rescale_f_10.setObjectName("label_rescale_f_10")
        self.label_rescale_f_10.setFont(font6)
        self.label_rescale_f_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_rescale_f_10, 3, 3, 1, 1)

        self.label_rescale_f_12 = QLabel(self.gridLayoutWidget)
        self.label_rescale_f_12.setObjectName("label_rescale_f_12")
        self.label_rescale_f_12.setFont(font6)
        self.label_rescale_f_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_rescale_f_12, 4, 3, 1, 1)

        self.gridLayout.setColumnStretch(0, 2)

        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        font8 = QFont()
        font8.setFamilies(["Lucida Sans"])
        font8.setPointSize(13)
        font8.setBold(True)
        self.groupBox_4.setFont(font8)
        self.formLayoutWidget_5 = QWidget(self.groupBox_4)
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(10, 30, 271, 191))
        self.formLayout_8 = QFormLayout(self.formLayoutWidget_5)
        self.formLayout_8.setObjectName("formLayout_8")
        self.formLayout_8.setVerticalSpacing(7)
        self.formLayout_8.setContentsMargins(0, 0, 15, 0)
        self.label_14 = QLabel(self.formLayoutWidget_5)
        self.label_14.setObjectName("label_14")
        font9 = QFont()
        font9.setFamilies(["Lucida Sans"])
        font9.setPointSize(10)
        font9.setBold(False)
        self.label_14.setFont(font9)

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.label_15 = QLabel(self.formLayoutWidget_5)
        self.label_15.setObjectName("label_15")
        self.label_15.setFont(font9)

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.label_16 = QLabel(self.formLayoutWidget_5)
        self.label_16.setObjectName("label_16")
        self.label_16.setFont(font9)

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.label_16)

        self.label_17 = QLabel(self.formLayoutWidget_5)
        self.label_17.setObjectName("label_17")

        self.formLayout_8.setWidget(4, QFormLayout.LabelRole, self.label_17)

        self.UM_label = QLabel(self.formLayoutWidget_5)
        self.UM_label.setObjectName("UM_label")
        self.UM_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_8.setWidget(4, QFormLayout.FieldRole, self.UM_label)

        self.label_19 = QLabel(self.formLayoutWidget_5)
        self.label_19.setObjectName("label_19")
        self.label_19.setFont(font9)

        self.formLayout_8.setWidget(5, QFormLayout.LabelRole, self.label_19)

        self.label_pref = QLabel(self.formLayoutWidget_5)
        self.label_pref.setObjectName("label_pref")
        self.label_pref.setFont(font9)
        self.label_pref.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.label_pref)

        self.output_label = QLabel(self.formLayoutWidget_5)
        self.output_label.setObjectName("output_label")
        self.output_label.setFont(font9)
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.output_label)

        self.ptoday_edit = QLineEdit(self.formLayoutWidget_5)
        self.ptoday_edit.setObjectName("ptoday_edit")
        self.ptoday_edit.setFont(font9)
        self.ptoday_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.ptoday_edit)

        self.SecondEdit = QLineEdit(self.formLayoutWidget_5)
        self.SecondEdit.setObjectName("SecondEdit")
        self.SecondEdit.setFont(font9)
        self.SecondEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_8.setWidget(5, QFormLayout.FieldRole, self.SecondEdit)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.formLayout_8.setItem(2, QFormLayout.LabelRole, self.horizontalSpacer)

        self.calcular = QPushButton(self.formLayoutWidget_5)
        self.calcular.setObjectName("calcular")
        icon1 = QIcon()
        icon1.addFile(
            ":/icons/res/calc-icon-blue.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.calcular.setIcon(icon1)

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.calcular)

        self.label_30 = QLabel(self.formLayoutWidget_5)
        self.label_30.setObjectName("label_30")
        self.label_30.setFont(font9)

        self.formLayout_8.setWidget(6, QFormLayout.LabelRole, self.label_30)

        self.desv_label = QLabel(self.formLayoutWidget_5)
        self.desv_label.setObjectName("desv_label")
        self.desv_label.setFont(font9)
        self.desv_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_8.setWidget(6, QFormLayout.FieldRole, self.desv_label)

        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.setFont(font8)
        self.groupBox_5.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.formLayoutWidget_4 = QWidget(self.groupBox_5)
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(10, 30, 271, 91))
        self.formLayout_7 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_7.setObjectName("formLayout_7")
        self.formLayout_7.setFormAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.formLayout_7.setHorizontalSpacing(6)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.formLayoutWidget_4)
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(font3)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.label_linac_energy = QLabel(self.formLayoutWidget_4)
        self.label_linac_energy.setObjectName("label_linac_energy")
        self.label_linac_energy.setFont(font3)
        self.label_linac_energy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.label_linac_energy)

        self.label_linac_applicator = QLabel(self.formLayoutWidget_4)
        self.label_linac_applicator.setObjectName("label_linac_applicator")
        self.label_linac_applicator.setFont(font3)
        self.label_linac_applicator.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_7.setWidget(
            1, QFormLayout.FieldRole, self.label_linac_applicator
        )

        self.label_8 = QLabel(self.formLayoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font3)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.label_linac_dose = QLabel(self.formLayoutWidget_4)
        self.label_linac_dose.setObjectName("label_linac_dose")
        self.label_linac_dose.setFont(font3)
        self.label_linac_dose.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.label_linac_dose)

        self.label_6 = QLabel(self.formLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(font3)

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.verticalLayout.addWidget(self.groupBox_5)

        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 5)
        self.verticalLayout.setStretch(4, 5)
        self.verticalLayout.setStretch(5, 3)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphWidget1 = GraphicsLayoutWidget(self.centralwidget)
        self.graphWidget1.setObjectName("graphWidget1")

        self.verticalLayout_3.addWidget(self.graphWidget1)

        self.graphWidget2 = GraphicsLayoutWidget(self.centralwidget)
        self.graphWidget2.setObjectName("graphWidget2")

        self.verticalLayout_3.addWidget(self.graphWidget2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.graphWidget3 = GraphicsLayoutWidget(self.centralwidget)
        self.graphWidget3.setObjectName("graphWidget3")

        self.horizontalLayout_7.addWidget(self.graphWidget3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        font10 = QFont()
        font10.setFamilies(["Lucida Sans"])
        self.label_13.setFont(font10)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.label_zmax = QLabel(self.centralwidget)
        self.label_zmax.setObjectName("label_zmax")
        self.label_zmax.setFont(font10)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_zmax)

        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName("label_34")
        self.label_34.setFont(font10)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_34)

        self.label_R90X = QLabel(self.centralwidget)
        self.label_R90X.setObjectName("label_R90X")
        self.label_R90X.setFont(font10)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_R90X)

        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName("label_32")
        self.label_32.setFont(font10)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_32)

        self.label_R90Y = QLabel(self.centralwidget)
        self.label_R90Y.setObjectName("label_R90Y")
        self.label_R90Y.setFont(font10)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_R90Y)

        self.horizontalLayout_7.addLayout(self.formLayout)

        self.horizontalLayout_7.setStretch(0, 5)
        self.horizontalLayout_7.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 4)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.openGLWidget = GLViewWidget(self.centralwidget)
        self.openGLWidget.setObjectName("openGLWidget")
        self.openGLWidget.setAutoFillBackground(True)

        self.verticalLayout_4.addWidget(self.openGLWidget)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        font11 = QFont()
        font11.setFamilies(["Lucida Sans"])
        font11.setPointSize(13)
        self.groupBox_6.setFont(font11)
        self.groupBox_6.setAutoFillBackground(False)
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_6)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 20, 481, 381))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 6, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_18 = QLabel(self.verticalLayoutWidget_4)
        self.label_18.setObjectName("label_18")
        font12 = QFont()
        font12.setFamilies(["Lucida Sans"])
        font12.setPointSize(10)
        self.label_18.setFont(font12)

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.NameEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.NameEdit.setObjectName("NameEdit")
        self.NameEdit.setFont(font12)

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.NameEdit)

        self.label_20 = QLabel(self.verticalLayoutWidget_4)
        self.label_20.setObjectName("label_20")
        self.label_20.setFont(font12)

        self.formLayout_9.setWidget(2, QFormLayout.LabelRole, self.label_20)

        self.IDEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.IDEdit.setObjectName("IDEdit")
        self.IDEdit.setFont(font12)

        self.formLayout_9.setWidget(2, QFormLayout.FieldRole, self.IDEdit)

        self.label_21 = QLabel(self.verticalLayoutWidget_4)
        self.label_21.setObjectName("label_21")
        self.label_21.setFont(font12)

        self.formLayout_9.setWidget(3, QFormLayout.LabelRole, self.label_21)

        self.SiteEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.SiteEdit.setObjectName("SiteEdit")
        self.SiteEdit.setFont(font12)

        self.formLayout_9.setWidget(3, QFormLayout.FieldRole, self.SiteEdit)

        self.label_22 = QLabel(self.verticalLayoutWidget_4)
        self.label_22.setObjectName("label_22")
        self.label_22.setFont(font12)

        self.formLayout_9.setWidget(4, QFormLayout.LabelRole, self.label_22)

        self.PhysicistEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.PhysicistEdit.setObjectName("PhysicistEdit")
        self.PhysicistEdit.setFont(font12)

        self.formLayout_9.setWidget(4, QFormLayout.FieldRole, self.PhysicistEdit)

        self.label_23 = QLabel(self.verticalLayoutWidget_4)
        self.label_23.setObjectName("label_23")
        self.label_23.setFont(font12)

        self.formLayout_9.setWidget(5, QFormLayout.LabelRole, self.label_23)

        self.OncologistEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.OncologistEdit.setObjectName("OncologistEdit")
        self.OncologistEdit.setFont(font12)

        self.formLayout_9.setWidget(5, QFormLayout.FieldRole, self.OncologistEdit)

        self.label_24 = QLabel(self.verticalLayoutWidget_4)
        self.label_24.setObjectName("label_24")
        self.label_24.setFont(font12)

        self.formLayout_9.setWidget(6, QFormLayout.LabelRole, self.label_24)

        self.TechnologistEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.TechnologistEdit.setObjectName("TechnologistEdit")
        self.TechnologistEdit.setFont(font12)

        self.formLayout_9.setWidget(6, QFormLayout.FieldRole, self.TechnologistEdit)

        self.label_31 = QLabel(self.verticalLayoutWidget_4)
        self.label_31.setObjectName("label_31")
        self.label_31.setFont(font12)

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.label_31)

        self.SurnameEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.SurnameEdit.setObjectName("SurnameEdit")
        self.SurnameEdit.setFont(font12)

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.SurnameEdit)

        self.horizontalLayout_3.addLayout(self.formLayout_9)

        self.line_2 = QFrame(self.verticalLayoutWidget_4)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_27 = QLabel(self.verticalLayoutWidget_4)
        self.label_27.setObjectName("label_27")
        self.label_27.setFont(font12)

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_27)

        self.PitchEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.PitchEdit.setObjectName("PitchEdit")
        self.PitchEdit.setFont(font12)

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.PitchEdit)

        self.label_28 = QLabel(self.verticalLayoutWidget_4)
        self.label_28.setObjectName("label_28")
        self.label_28.setFont(font12)

        self.formLayout_10.setWidget(1, QFormLayout.LabelRole, self.label_28)

        self.RollEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.RollEdit.setObjectName("RollEdit")
        self.RollEdit.setFont(font12)

        self.formLayout_10.setWidget(1, QFormLayout.FieldRole, self.RollEdit)

        self.label_29 = QLabel(self.verticalLayoutWidget_4)
        self.label_29.setObjectName("label_29")
        self.label_29.setFont(font12)

        self.formLayout_10.setWidget(2, QFormLayout.LabelRole, self.label_29)

        self.VerticalEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.VerticalEdit.setObjectName("VerticalEdit")
        self.VerticalEdit.setFont(font12)

        self.formLayout_10.setWidget(2, QFormLayout.FieldRole, self.VerticalEdit)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.formLayout_10.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.formLayout_10.setItem(5, QFormLayout.LabelRole, self.verticalSpacer)

        self.label_25 = QLabel(self.verticalLayoutWidget_4)
        self.label_25.setObjectName("label_25")
        self.label_25.setFont(font12)

        self.formLayout_10.setWidget(4, QFormLayout.LabelRole, self.label_25)

        self.IORTnumberEdit = QLineEdit(self.verticalLayoutWidget_4)
        self.IORTnumberEdit.setObjectName("IORTnumberEdit")
        self.IORTnumberEdit.setFont(font12)

        self.formLayout_10.setWidget(4, QFormLayout.FieldRole, self.IORTnumberEdit)

        self.horizontalLayout_3.addLayout(self.formLayout_10)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.verticalLayoutWidget_4)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_comments = QLabel(self.verticalLayoutWidget_4)
        self.label_comments.setObjectName("label_comments")

        self.horizontalLayout_8.addWidget(self.label_comments)

        self.label_comments_ico = QLabel(self.verticalLayoutWidget_4)
        self.label_comments_ico.setObjectName("label_comments_ico")
        sizePolicy.setHeightForWidth(
            self.label_comments_ico.sizePolicy().hasHeightForWidth()
        )
        self.label_comments_ico.setSizePolicy(sizePolicy)
        self.label_comments_ico.setMinimumSize(QSize(16, 16))
        self.label_comments_ico.setMaximumSize(QSize(20, 20))
        self.label_comments_ico.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_comments_ico)

        self.label_comments_warning = QLabel(self.verticalLayoutWidget_4)
        self.label_comments_warning.setObjectName("label_comments_warning")
        self.label_comments_warning.setFont(font12)

        self.horizontalLayout_8.addWidget(self.label_comments_warning)

        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 1)
        self.horizontalLayout_8.setStretch(2, 6)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.CommentsEdit = QPlainTextEdit(self.verticalLayoutWidget_4)
        self.CommentsEdit.setObjectName("CommentsEdit")
        self.CommentsEdit.setFont(font12)

        self.horizontalLayout_4.addWidget(self.CommentsEdit)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, -1, -1, -1)
        self.pushreport = QPushButton(self.verticalLayoutWidget_4)
        self.pushreport.setObjectName("pushreport")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushreport.sizePolicy().hasHeightForWidth())
        self.pushreport.setSizePolicy(sizePolicy2)
        self.pushreport.setFont(font4)
        icon2 = QIcon()
        icon2.addFile(
            ":/icons/res/generate-report-icon-blue.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.pushreport.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushreport)

        self.pushsend = QPushButton(self.verticalLayoutWidget_4)
        self.pushsend.setObjectName("pushsend")
        self.pushsend.setFont(font4)
        icon3 = QIcon()
        icon3.addFile(
            ":/icons/res/curved-arrow-icon.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.pushsend.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pushsend)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.verticalLayout_4.addWidget(self.groupBox_6)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 5)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1468, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.combo_applicator, self.combo_bevel)
        QWidget.setTabOrder(self.combo_bevel, self.DoseEdit)
        QWidget.setTabOrder(self.DoseEdit, self.depth_edit)
        QWidget.setTabOrder(self.depth_edit, self.radio1)
        QWidget.setTabOrder(self.radio1, self.radio2)
        QWidget.setTabOrder(self.radio2, self.radio3)
        QWidget.setTabOrder(self.radio3, self.radio4)
        QWidget.setTabOrder(self.radio4, self.ptoday_edit)
        QWidget.setTabOrder(self.ptoday_edit, self.calcular)
        QWidget.setTabOrder(self.calcular, self.SecondEdit)
        QWidget.setTabOrder(self.SecondEdit, self.NameEdit)
        QWidget.setTabOrder(self.NameEdit, self.SurnameEdit)
        QWidget.setTabOrder(self.SurnameEdit, self.IDEdit)
        QWidget.setTabOrder(self.IDEdit, self.SiteEdit)
        QWidget.setTabOrder(self.SiteEdit, self.PhysicistEdit)
        QWidget.setTabOrder(self.PhysicistEdit, self.OncologistEdit)
        QWidget.setTabOrder(self.OncologistEdit, self.TechnologistEdit)
        QWidget.setTabOrder(self.TechnologistEdit, self.PitchEdit)
        QWidget.setTabOrder(self.PitchEdit, self.RollEdit)
        QWidget.setTabOrder(self.RollEdit, self.VerticalEdit)
        QWidget.setTabOrder(self.VerticalEdit, self.IORTnumberEdit)
        QWidget.setTabOrder(self.IORTnumberEdit, self.CommentsEdit)
        QWidget.setTabOrder(self.CommentsEdit, self.pushreport)
        QWidget.setTabOrder(self.pushreport, self.pushsend)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Kali MC", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:16pt; color:#55aaff;">KALI MC - LIAC HWL</span></p></body></html>',
                None,
            )
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("MainWindow", "Aplicador", None)
        )
        self.combo_applicator.setItemText(0, "")
        self.combo_applicator.setItemText(
            1, QCoreApplication.translate("MainWindow", "12", None)
        )
        self.combo_applicator.setItemText(
            2, QCoreApplication.translate("MainWindow", "10", None)
        )
        self.combo_applicator.setItemText(
            3, QCoreApplication.translate("MainWindow", "9", None)
        )
        self.combo_applicator.setItemText(
            4, QCoreApplication.translate("MainWindow", "8", None)
        )
        self.combo_applicator.setItemText(
            5, QCoreApplication.translate("MainWindow", "7", None)
        )
        self.combo_applicator.setItemText(
            6, QCoreApplication.translate("MainWindow", "6", None)
        )
        self.combo_applicator.setItemText(
            7, QCoreApplication.translate("MainWindow", "5", None)
        )
        self.combo_applicator.setItemText(
            8, QCoreApplication.translate("MainWindow", "4", None)
        )
        self.combo_applicator.setItemText(
            9, QCoreApplication.translate("MainWindow", "3", None)
        )

        self.combo_bevel.setItemText(0, "")
        self.combo_bevel.setItemText(
            1, QCoreApplication.translate("MainWindow", "0", None)
        )
        self.combo_bevel.setItemText(
            2, QCoreApplication.translate("MainWindow", "15", None)
        )
        self.combo_bevel.setItemText(
            3, QCoreApplication.translate("MainWindow", "30", None)
        )
        self.combo_bevel.setItemText(
            4, QCoreApplication.translate("MainWindow", "45", None)
        )

        self.label_9.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Bisel", None))
        self.label_12.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Cono", None))
        self.groupBox_2.setTitle(
            QCoreApplication.translate("MainWindow", "Prescripci\u00f3n", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", "Dosis (cGy)", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "Profundidad (cm)", None)
        )
        self.groupBox_3.setTitle(
            QCoreApplication.translate("MainWindow", "Energ\u00edas", None)
        )
        self.label_12MeV.setText("")
        # if QT_CONFIG(tooltip)
        self.label_rescale_ico_12.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "CUIDADO! No se recomienda usar esta combinaci\u00f3n de cono/bisel y energ\u00eda",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.label_rescale_ico_12.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.label_rescale_ico_12.setText("")
        self.label_11.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>R<span style=" vertical-align:sub;">90</span> (cm)</p></body></html>',
                None,
            )
        )
        self.label_8MeV.setText("")
        # if QT_CONFIG(tooltip)
        self.label_rescale_ico_6.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.label_rescale_ico_6.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.label_rescale_ico_6.setText("")
        # if QT_CONFIG(tooltip)
        self.label_rescale_ico_10.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "CUIDADO! No se recomienda usar esta combinaci\u00f3n de cono/bisel y energ\u00eda",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.label_rescale_ico_10.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.label_rescale_ico_10.setText("")
        self.radio4.setText(QCoreApplication.translate("MainWindow", "12 MeV", None))
        self.radio1.setText(QCoreApplication.translate("MainWindow", "6 MeV", None))
        self.radio3.setText(QCoreApplication.translate("MainWindow", "10 MeV", None))
        self.label_6MeV.setText("")
        self.label_10MeV.setText("")
        self.radio2.setText(QCoreApplication.translate("MainWindow", "8 MeV", None))
        # if QT_CONFIG(tooltip)
        self.label_rescale_ico_8.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "CUIDADO! No se recomienda usar esta combinaci\u00f3n de cono/bisel y energ\u00eda",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.label_rescale_ico_8.setWhatsThis("")
        # endif // QT_CONFIG(whatsthis)
        self.label_rescale_ico_8.setText("")
        self.label_rescale_f_8.setText("")
        self.label_35.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p align="center">Factor<br/>de<br/>reescalado</p></body></html>',
                None,
            )
        )
        self.label_rescale_f_6.setText("")
        self.label_rescale_f_10.setText("")
        self.label_rescale_f_12.setText("")
        self.groupBox_4.setTitle(
            QCoreApplication.translate("MainWindow", "C\u00e1lculo de UM", None)
        )
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", "Pref (hPa):", None)
        )
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", "Phoy (hPa):", None)
        )
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "cGy/UM Pref:", None)
        )
        self.label_17.setText(QCoreApplication.translate("MainWindow", "UM:", None))
        self.UM_label.setText("")
        self.label_19.setText(
            QCoreApplication.translate("MainWindow", "UM 2\u00ba c\u00e1lculo:", None)
        )
        self.label_pref.setText("")
        self.output_label.setText("")
        self.calcular.setText(
            QCoreApplication.translate("MainWindow", " CALCULAR", None)
        )
        self.label_30.setText(
            QCoreApplication.translate("MainWindow", "Desv. (%):", None)
        )
        self.desv_label.setText("")
        self.groupBox_5.setTitle("")
        self.label_7.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">Energy</span></p></body></html>',
                None,
            )
        )
        self.label_linac_energy.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">0 MeV</span></p></body></html>',
                None,
            )
        )
        self.label_linac_applicator.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">Appl</span></p></body></html>',
                None,
            )
        )
        self.label_8.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">Appl</span></p></body></html>',
                None,
            )
        )
        self.label_linac_dose.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">0</span></p></body></html>',
                None,
            )
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:12pt; color:#ffffff;">Dose</span></p></body></html>',
                None,
            )
        )
        self.label_13.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>z<span style=" vertical-align:sub;">max</span> (cm):</p></body></html>',
                None,
            )
        )
        self.label_zmax.setText("")
        self.label_34.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>X R<span style=" vertical-align:sub;">90</span> (cm):</p></body></html>',
                None,
            )
        )
        self.label_R90X.setText("")
        self.label_32.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Y R<span style=" vertical-align:sub;">90</span> (cm):</p></body></html>',
                None,
            )
        )
        self.label_R90Y.setText("")
        self.groupBox_6.setTitle(
            QCoreApplication.translate("MainWindow", "Datos Administrativos", None)
        )
        self.label_18.setText(QCoreApplication.translate("MainWindow", "Nombre:", None))
        self.label_20.setText(
            QCoreApplication.translate("MainWindow", "N\u00ba de Historia:", None)
        )
        self.label_21.setText(
            QCoreApplication.translate("MainWindow", "Localizaci\u00f3n:", None)
        )
        self.label_22.setText(
            QCoreApplication.translate("MainWindow", "Radiof\u00edsico:", None)
        )
        self.label_23.setText(
            QCoreApplication.translate("MainWindow", "O. Radioter\u00e1pico:", None)
        )
        self.label_24.setText(QCoreApplication.translate("MainWindow", "T.E.R.t", None))
        self.label_31.setText(
            QCoreApplication.translate("MainWindow", "Apellidos:", None)
        )
        self.label_27.setText(
            QCoreApplication.translate("MainWindow", "Pitch (\u00ba):", None)
        )
        self.label_28.setText(
            QCoreApplication.translate("MainWindow", "Roll (\u00ba):", None)
        )
        self.label_29.setText(
            QCoreApplication.translate("MainWindow", "Esc. vert. (cm):", None)
        )
        self.label_25.setText(
            QCoreApplication.translate("MainWindow", "N\u00ba de RIO:", None)
        )
        self.label_comments.setText(
            QCoreApplication.translate("MainWindow", "Incidencias:", None)
        )
        self.label_comments_ico.setText("")
        self.label_comments_warning.setText("")
        self.CommentsEdit.setPlainText("")
        self.pushreport.setText(
            QCoreApplication.translate("MainWindow", "Generar Informe", None)
        )
        self.pushsend.setText(
            QCoreApplication.translate("MainWindow", "Enviar RTPlan", None)
        )

    # retranslateUi
