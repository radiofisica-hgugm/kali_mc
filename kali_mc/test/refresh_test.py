import pytest
from unittest.mock import MagicMock, patch
from PySide6 import QtGui
import numpy as np
from kali_mc.main import Window


def test_refresh_valid_indices_and_rescale_warning(qtbot, mocker):
    """Test refresh method with valid indices and rescale warning condition."""
    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    # Set up mock data for GUI elements and return values
    mocker.patch.object(window.combo_applicator, "currentIndex", return_value=7)
    mocker.patch.object(window.combo_applicator, "currentText", return_value="6")
    mocker.patch.object(window.combo_bevel, "currentIndex", return_value=2)
    mocker.patch.object(window.combo_bevel, "currentText", return_value="0")
    mocker.patch.object(window.ptoday_edit, "text", return_value="")
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

    # Mock np.load to return expected arrays
    mock_r90_array = MagicMock()
    mock_r90_array.__getitem__.side_effect = lambda x: [1.5, 1.9, 2.4, 2.8]
    mock_npz_file = {
        "R90": mock_r90_array,
        "SpatialDoseDistrib": MagicMock(return_value={}),  # Mock dose distribution data
    }
    mocker.patch("numpy.load", return_value=mock_npz_file)

    # Mock the rescale_mat attribute
    window.rescale_mat = np.ones([36, 4]) + 0.015

    # Mock plot_distribs to confirm it’s called without plotting
    plot_distribs_mock = mocker.patch.object(window, "plot_distribs")

    # Call the method
    window.refresh()

    # Verify labels were set correctly based on R90_array values
    assert window.label_6MeV.text() == "1.5"
    assert window.label_8MeV.text() == "1.9"
    assert window.label_10MeV.text() == "2.4"
    assert window.label_12MeV.text() == "2.8"

    # Verify that warnings and icons are set based on rescale_mat values
    assert (
        window.label_rescale_ico_10.toolTip()
        == "CUIDADO! se aplicará un factor de reescalado"
    )
    assert (
        window.label_rescale_ico_10.pixmap() is not None
    )  # Confirm that an icon is set
    assert window.label_rescale_ico_12.pixmap().width() > 0

    # Check that plot_distribs was called
    plot_distribs_mock.assert_called_once()


def test_refresh_recaling_danger(qtbot, mocker):
    """Test refresh method with rescale danger condition."""
    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    # Set up mock data for GUI elements and return values
    mocker.patch.object(window.combo_applicator, "currentIndex", return_value=7)
    mocker.patch.object(window.combo_applicator, "currentText", return_value="6")
    mocker.patch.object(window.combo_bevel, "currentIndex", return_value=2)
    mocker.patch.object(window.combo_bevel, "currentText", return_value="0")
    mocker.patch.object(window.ptoday_edit, "text", return_value="")
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

    # Mock np.load to return expected arrays
    mock_r90_array = MagicMock()
    mock_r90_array.__getitem__.side_effect = lambda x: [1.5, 1.9, 2.4, 2.8]
    mock_npz_file = {
        "R90": mock_r90_array,
        "SpatialDoseDistrib": MagicMock(return_value={}),  # Mock dose distribution data
    }
    mocker.patch("numpy.load", return_value=mock_npz_file)

    # Mock the rescale_mat attribute
    window.rescale_mat = np.zeros([36, 4])

    # Mock plot_distribs to confirm it’s called without plotting
    plot_distribs_mock = mocker.patch.object(window, "plot_distribs")

    # Call the method
    window.refresh()

    # Verify that warnings and icons are set based on rescale_mat values
    assert (
        window.label_rescale_ico_12.toolTip()
        == "CUIDADO! No se recomienda usar esta combinación de cono/bisel y energía"
    )
    assert (
        window.label_rescale_ico_12.pixmap() is not None
    )  # Confirm that an icon is set
    assert (
        window.label_rescale_ico_12.pixmap().width() > 0
    )  # Confirm that no icon is set

    # Check that plot_distribs was called
    plot_distribs_mock.assert_called_once()


def test_refresh_rescaling_no_warning(qtbot, mocker):
    """Test refresh method with no warning condition."""
    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    # Set up mock data for GUI elements and return values
    mocker.patch.object(window.combo_applicator, "currentIndex", return_value=7)
    mocker.patch.object(window.combo_applicator, "currentText", return_value="6")
    mocker.patch.object(window.combo_bevel, "currentIndex", return_value=2)
    mocker.patch.object(window.combo_bevel, "currentText", return_value="0")
    mocker.patch.object(window.ptoday_edit, "text", return_value="")
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

    # Mock np.load to return expected arrays
    mock_r90_array = MagicMock()
    mock_r90_array.__getitem__.side_effect = lambda x: [1.5, 1.9, 2.4, 2.8]
    mock_npz_file = {
        "R90": mock_r90_array,
        "SpatialDoseDistrib": MagicMock(return_value={}),  # Mock dose distribution data
    }
    mocker.patch("numpy.load", return_value=mock_npz_file)

    # Mock the rescale_mat attribute
    window.rescale_mat = np.ones([36, 4])

    # Mock plot_distribs to confirm it’s called without plotting
    plot_distribs_mock = mocker.patch.object(window, "plot_distribs")

    # Call the method
    window.refresh()

    # Verify that warnings and icons are set based on rescale_mat values
    assert window.label_rescale_ico_12.toolTip() == ""
    assert (
        window.label_rescale_ico_12.pixmap().width() == 0
    )  # Confirm that no icon is set

    # Check that plot_distribs was called
    plot_distribs_mock.assert_called_once()


def test_refresh_no_selection(qtbot, mocker):
    """Test refresh method with insufficient input data (no dose loaded)."""
    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    # Set up mock data for GUI elements and return values
    mocker.patch.object(
        window.combo_applicator, "currentIndex", return_value=0
    )  # No selection
    mocker.patch.object(window.combo_applicator, "currentText", return_value="")
    mocker.patch.object(window.combo_bevel, "currentIndex", return_value=0)
    mocker.patch.object(window.combo_bevel, "currentText", return_value="")
    mocker.patch.object(window.ptoday_edit, "text", return_value="")
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
        window.radio4, "isChecked", return_value=False
    )  # Energy = 12 MeV

    # Call the method
    window.refresh()

    # Assert that no dose matrix is loaded
    assert window.npzfile == ""
    assert window.dose_distrib is None
