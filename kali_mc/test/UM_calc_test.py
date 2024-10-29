import pytest
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMessageBox
from main import Window  # Import your class from your module
import numpy as np


def test_calculate_UM(qtbot, mocker):
    """Test the calculate_something method with mocked input values."""

    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    # Mock the QComboBox and QLineEdit values

    mocker.patch.object(window.DoseEdit, "text", return_value="1250")  # Dose = 1250 cGy
    mocker.patch.object(
        window.combo_applicator, "currentText", return_value="5"
    )  # Applicator -> 5 cm
    mocker.patch.object(
        window.combo_bevel, "currentIndex", return_value=4
    )  # Bevel -> 45º
    mocker.patch.object(
        window.radio4, "isChecked", return_value=True
    )  # Energy = 12 MeV
    mocker.patch.object(
        window.ptoday_edit, "text", return_value="950"
    )  # Current air pressure = 950 hPa

    # Call the method
    window.calculate_UM()

    # Assert that the result is as expected
    assert window.UM_label.text() == "920"
    assert window.output_label.text() == "1.534"
    assert window.label_linac_applicator.text() == "50 mm"
    assert window.label_linac_dose.text() == "920 UM"
    assert window.label_linac_energy.text() == "12 MeV"


def test_calculate_UM_rescale(qtbot, mocker):
    """Test the calculate_UM method with mocked input values and rescaling factors"""

    mocker.patch("main.rescale_factors", True)
    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    # Mock the QComboBox and QLineEdit values

    mocker.patch.object(window.DoseEdit, "text", return_value="1250")  # Dose = 1250 cGy
    mocker.patch.object(
        window.combo_applicator, "currentText", return_value="12"
    )  # Applicator -> 12 cm
    mocker.patch.object(window.combo_applicator, "currentIndex", return_value=1)
    mocker.patch.object(
        window.combo_bevel, "currentIndex", return_value=1
    )  # Bevel -> 0º
    mocker.patch.object(
        window.combo_bevel, "currentText", return_value="0"
    )  # Applicator -> 12 cm
    mocker.patch.object(window.radio2, "isChecked", return_value=True)  # Energy = 8 MeV
    mocker.patch.object(
        window.ptoday_edit, "text", return_value="950"
    )  # Current air pressure = 950 hPa

    # Call the method
    window.refresh()
    window.calculate_UM()

    # Assert that the result is as expected
    assert window.UM_label.text() == "1679"
    assert window.output_label.text() == "0.883"
    assert window.label_linac_applicator.text() == "120 mm"
    assert window.label_linac_dose.text() == "1679 UM"
    assert window.label_linac_energy.text() == "8 MeV"
    assert window.rescale_factor == 1.05


def test_calculate_UM_rescale_disabled(qtbot, mocker):
    """Test the calculate_UM method with mocked input values and a disabled applicator/bevel/energy combination"""

    mocker.patch("main.rescale_factors", True)
    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    # Mock the QComboBox and QLineEdit values

    mocker.patch.object(window.DoseEdit, "text", return_value="1250")  # Dose = 1250 cGy
    mocker.patch.object(
        window.combo_applicator, "currentText", return_value="12"
    )  # Applicator -> 12 cm
    mocker.patch.object(window.combo_applicator, "currentIndex", return_value=1)
    mocker.patch.object(
        window.combo_bevel, "currentIndex", return_value=1
    )  # Bevel -> 0º
    mocker.patch.object(
        window.combo_bevel, "currentText", return_value="0"
    )  # Applicator -> 12 cm
    mocker.patch.object(
        window.radio3, "isChecked", return_value=True
    )  # Energy = 10 MeV
    mocker.patch.object(
        window.ptoday_edit, "text", return_value="950"
    )  # Current air pressure = 950 hPa

    # Call the method
    window.refresh()
    window.calculate_UM()

    # Assert that the result is as expected
    assert window.UM_label.text() == "0"
    assert window.output_label.text() == "0.888"
    assert window.label_linac_applicator.text() == "120 mm"
    assert window.label_linac_dose.text() == "0 UM"
    assert window.label_linac_energy.text() == "10 MeV"
    assert window.rescale_factor == 0


def test_calculate_um_invalid_dose_value(qtbot, mocker):
    """Test that a critical QMessageBox is shown when an invalid dose is entered."""

    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    # Mock the DoseEdit to return an invalid value that triggers ValueError
    mocker.patch.object(window.DoseEdit, "text", return_value="1,250")  # Invalid float

    # Mock QMessageBox to prevent it from showing in the test
    mock_box = mocker.patch.object(QMessageBox, "critical")

    # Call the method
    window.calculate_UM()

    # Assert that QMessageBox.critical was called with the correct parameters
    mock_box.assert_called_once_with(
        window,
        "Valor de dosis erróneo",
        "Error en valor de dosis introducida! Recuerda usar . como separador decimal",
    )


def test_calculate_um_high_dose(qtbot, mocker):
    """Test that a critical QMessageBox is shown when the dose is too high."""

    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    # Mock the DoseEdit to return a value higher than 3000
    mocker.patch.object(window.DoseEdit, "text", return_value="3500")

    # Mock QMessageBox to prevent it from showing in the test
    mock_box = mocker.patch.object(QMessageBox, "critical")

    # Call the method
    window.calculate_UM()

    # Assert that QMessageBox.critical was called with the correct parameters
    mock_box.assert_called_once_with(
        window, "Valor de dosis erróneo", "La dosis prescrita es demasiado alta!"
    )


def test_calculate_um_invalid_pressure_value(qtbot, mocker):
    """Test that a critical QMessageBox is shown when an invalid pressure is entered."""

    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    mocker.patch.object(window.DoseEdit, "text", return_value="1250")
    # Mock the ptoday_edit to return an invalid value that triggers ValueError
    mocker.patch.object(
        window.ptoday_edit, "text", return_value="9,50"
    )  # Invalid float

    # Mock QMessageBox to prevent it from showing in the test
    mock_box = mocker.patch.object(QMessageBox, "critical")

    # Call the method
    window.calculate_UM()

    # Assert that QMessageBox.critical was called with the correct parameters
    mock_box.assert_called_once_with(
        window,
        "Valor de presión erróneo",
        "Error en valor de presión introducida! Recuerda usar . como separador decimal",
    )


def test_calculate_um_out_of_range_pressure_value(qtbot, mocker):
    """Test that a critical QMessageBox is shown when an invalid pressure is entered."""

    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    mocker.patch.object(window.DoseEdit, "text", return_value="1250")
    # Mock the ptoday_edit to return an invalid value that triggers ValueError
    mocker.patch.object(
        window.ptoday_edit, "text", return_value="1950"
    )  # Invalid float

    # Mock QMessageBox to prevent it from showing in the test
    mock_box = mocker.patch.object(QMessageBox, "critical")

    # Call the method
    window.calculate_UM()

    # Assert that QMessageBox.critical was called with the correct parameters
    mock_box.assert_called_once_with(
        window,
        "Valor de presión erróneo",
        "La presión introducida es incorrecta",
    )


def test_calc_um_diff_valid_values(qtbot, mocker):
    """Test calc_UM_diff with valid numeric input values."""

    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    # Mock the text of UM_label and SecondEdit
    mocker.patch.object(window.UM_label, "text", return_value="100.0")
    mocker.patch.object(window.SecondEdit, "text", return_value="110.0")

    # Call the method
    window.calc_UM_diff()

    # Assert the expected output in desv_label
    expected_desv = ((110.0 - 100.0) / 100.0) * 100  # Expected to be 10.0
    assert window.desv_label.text() == f"{expected_desv:.1f}"


def test_calc_um_diff_empty_values(qtbot, mocker):
    """Test calc_UM_diff with empty input values, expecting no update to desv_label."""

    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    # Mock empty text for UM_label and SecondEdit
    mocker.patch.object(window.UM_label, "text", return_value="")
    mocker.patch.object(window.SecondEdit, "text", return_value="")

    # Call the method
    window.calc_UM_diff()

    # Assert that desv_label was not updated (empty text or default state)
    assert window.desv_label.text() == ""


def test_rescale_factors_disabled(qtbot, mocker):
    """Test to verify that when rescaled factors are disabled self.rescale_mat == ones([36,4])"""

    mocker.patch("main.rescale_factors", False)
    # Create the window instance
    window = Window()
    qtbot.addWidget(window)

    assert window.rescale_mat.any() == 1.0
