import pytest
import datetime
from unittest.mock import MagicMock, patch
from pydicom.dataset import Dataset
from pydicom.uid import ImplicitVRLittleEndian
from pynetdicom import AE
from kali_mc.main import Window
from kali_mc.dicom_utils import fill_rtplan
import tempfile

destination_server = "localhost"
destination_port = 104
destination_AETitle = "AETitle"


def create_fake_data_dict():
    data_dict = {
        "Name": "Gustave",
        "Surname": "Flaubert",
        "ID": "3456734",
        "Site": "Sarcoma Retroperitoneal",
        "Physicist": "Luis de Góngora y Argote",
        "Oncologist": "Honoré de Balzac",
        "TERt": "Victor Hugo, Francisco de Quevedo y Villegas",
        "Date": datetime.date.today(),
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
        "Pitch": 3,
        "Roll": 10,
        "Vertical": 220,
        "IORT_number": "2999",
        "Comments": "No habido problemas con la irradiación, Si la línea es muy larga es posible que "
        "se salga del recuadro. Un poco más de información para ver cómo se rellena",
    }
    return data_dict


def test_fill_rtplan_creates_rtplan_with_required_fields():
    # Sample data_dict with required fields
    data_dict = create_fake_data_dict()

    # Use a temporary file as in the original function
    with tempfile.TemporaryFile() as fp:
        rtplan = fill_rtplan(fp, data_dict)

    # Verify that rtplan contains the required DICOM fields
    required_fields = [
        "PatientName",
        "PatientID",
        "Modality",
        "StudyInstanceUID",
        "SeriesInstanceUID",
        "SOPInstanceUID",
        "SOPClassUID",
    ]
    for field in required_fields:
        assert hasattr(rtplan, field), f"{field} is missing in rtplan"
    # Optionally: Add further assertions to check specific values


def test_send_dicom_with_real_rtplan_creation(qtbot, mocker):
    # Initialize the window instance
    window = Window()
    qtbot.addWidget(window)

    mocker.patch.object(
        window, "create_data_dict", return_value=create_fake_data_dict()
    )

    # Mock the AE class in dicom_utils.py
    mock_ae = mocker.patch("dicom_utils.AE")

    # Configure the mocked AE instance behavior
    mock_ae_instance = mock_ae.return_value
    mock_assoc = mock_ae_instance.associate.return_value
    mock_assoc.is_established = True

    # Mock the status returned by send_c_store
    mock_status = MagicMock()
    mock_status.Status = 0  # Simulate success status
    mock_assoc.send_c_store.return_value = mock_status

    # Run the send_dicom method
    window.send_dicom()

    # Verify send_c_store was called
    assert mock_assoc.send_c_store.called, "send_c_store was not called as expected."
    # Verify release was called to end the association
    mock_assoc.release.assert_called_once()
