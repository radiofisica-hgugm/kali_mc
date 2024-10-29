import datetime
import os
import tempfile
from unittest.mock import MagicMock, patch
from kali_mc.report_utils import create_pdf
from main import Window


def create_fake_data_dict():
    data_dict = {
        "Name": "Gustave",
        "Surname": "Flaubert",
        "ID": "3456734",
        "Site": "Sarcoma Retroperitoneal",
        "Physicist": "Luis de Góngora y Argote",
        "Oncologist": "Honoré de Balzac",
        "TERt": "Victor Hugo, Francisco de Quevedo y Villegas",
        "Date": f'{datetime.date.today().strftime("%d-%m-%Y")}',
        "Applicator": "10",
        "Bevel": "45",
        "Dose": "1250",
        "R90": "1.45",
        "Pressure": "942",
        "RefPressure": "934.7",
        "Energy": 10,
        "Beam_R90": 1.5,
        "Beam_zmax": 0.94,
        "Output": 1.1,
        "Rescale_factor": 1.0,
        "UM": 2500,
        "R90X": 3.0,
        "R90Y": 3.5,
        "UM2": 2505,
        "UM_dev": 0.5,
        "Linac": "LIAC HWL 0000",
        "Pitch": "3",
        "Roll": "10",
        "Vertical": "220",
        "IORT_number": "2999",
        "Comments": "No habido problemas con la irradiación, Si la línea es muy larga es posible que "
        "se salga del recuadro. Un poco más de información para ver cómo se rellena",
    }
    return data_dict


def test_report():
    filepath = os.path.dirname(__file__)
    data_dict = create_fake_data_dict()
    create_pdf(
        os.path.join(filepath, "report_test.pdf"),
        os.path.join(filepath, "cross.png"),
        os.path.join(filepath, "in.png"),
        os.path.join(filepath, "coronal.png"),
        os.path.join(filepath, "3D.png"),
        data_dict,
    )
    assert os.path.isfile(os.path.join(filepath, "report_test.pdf"))


def test_generate_report(qtbot, mocker):

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

    mock_file_dialog = mocker.patch(
        "PySide6.QtWidgets.QFileDialog.getSaveFileName",
        return_value=("test_report.pdf", ""),
    )

    # Mock the ImageExporter and OpenGLWidget to avoid actual file creation and image grabbing
    mock_exporter = MagicMock()
    mocker.patch("pyqtgraph.exporters.ImageExporter", return_value=mock_exporter)

    filepath = os.path.dirname(__file__)
    mock_create_pdf = mocker.patch("main.create_pdf")

    # Mock grabFramebuffer() to avoid OpenGL rendering issues
    mock_grab_framebuffer = mocker.patch.object(
        window.openGLWidget, "grabFramebuffer", return_value=MagicMock()
    )

    window.generate_report()

    # Check QFileDialog called as expected
    mock_file_dialog.assert_called_once()
    # Check create_pdf was called with the correct arguments
    mock_create_pdf.assert_called_once()

    # Test case where QFileDialog returns an empty path (cancelled)
    with patch("PySide6.QtWidgets.QFileDialog.getSaveFileName", return_value=("", "")):
        # Reset the mock calls for a fresh test
        mock_create_pdf.reset_mock()

        # Call generate_report
        window.generate_report()

        # Ensure create_pdf was not called
        mock_create_pdf.assert_not_called()
