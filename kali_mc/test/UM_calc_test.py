from kali_mc.main import Window  # Import your class from your module


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
