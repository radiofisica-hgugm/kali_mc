from main import Window
from unittest.mock import MagicMock
import numpy as np


def test_plot_distribs(qtbot, mocker):
    # Initialize the window instance
    window = Window()
    qtbot.addWidget(window)

    mocker.patch.object(window.DoseEdit, "text", return_value="1250")  # Dose = 1250 cGy
    mocker.patch.object(window.combo_applicator, "currentIndex", return_value=7)
    mocker.patch.object(window.combo_applicator, "currentText", return_value="6")
    mocker.patch.object(window.combo_bevel, "currentIndex", return_value=4)
    mocker.patch.object(window.combo_bevel, "currentText", return_value="45")
    mocker.patch.object(
        window.radio1, "isChecked", return_value=False
    )  # Energy = 6 MeV
    mocker.patch.object(
        window.radio2, "isChecked", return_value=False
    )  # Energy = 8 MeV
    mocker.patch.object(
        window.radio3, "isChecked", return_value=False
    )  # Energy = 10 MeV
    mocker.patch.object(
        window.radio4, "isChecked", return_value=True
    )  # Energy = 12 MeV
    mocker.patch.object(
        window.ptoday_edit, "text", return_value="950"
    )  # Current air pressure = 950 hPa

    # Run the plot_distribs method
    window.refresh()

    # Verify size of images or number of elements in widget
    assert window.p1.items[0].image.size == 4760
    assert window.p2.items[0].image.size == 4216
    assert window.p3.items[0].image.size == 4340
    assert len(window.openGLWidget.items) == 5


def test_plot_distribs_rescaling_zero(qtbot, mocker):
    # Initialize the window instance
    window = Window()
    qtbot.addWidget(window)

    mocker.patch.object(window.DoseEdit, "text", return_value="1250")  # Dose = 1250 cGy
    mocker.patch.object(window.combo_applicator, "currentIndex", return_value=7)
    mocker.patch.object(window.combo_applicator, "currentText", return_value="6")
    mocker.patch.object(window.combo_bevel, "currentIndex", return_value=4)
    mocker.patch.object(window.combo_bevel, "currentText", return_value="45")
    mocker.patch.object(
        window.radio1, "isChecked", return_value=False
    )  # Energy = 6 MeV
    mocker.patch.object(
        window.radio2, "isChecked", return_value=False
    )  # Energy = 8 MeV
    mocker.patch.object(
        window.radio3, "isChecked", return_value=False
    )  # Energy = 10 MeV
    mocker.patch.object(
        window.radio4, "isChecked", return_value=True
    )  # Energy = 12 MeV
    mocker.patch.object(
        window.ptoday_edit, "text", return_value="950"
    )  # Current air pressure = 950 hPa

    # Mock the rescale_mat attribute
    window.rescale_mat = np.zeros([36, 4])
    # Run the plot_distribs method
    window.refresh()

    # Verify that all p1, p2, p3 and openGLWidget are cleared
    assert len(window.p1.items) == 0
    assert len(window.p2.items) == 0
    assert len(window.p3.items) == 0
    assert len(window.openGLWidget.items) == 0
