import pytest
import datetime
from unittest.mock import MagicMock, patch
from pydicom.dataset import Dataset
from pydicom.uid import ImplicitVRLittleEndian
from pynetdicom import AE
from kali_mc.main import Window

# destination_server = 'localhost'
# destination_port = 104
# destination_AETitle = 'AETitle'


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


def test_send_dicom_with_real_rtplan_creation(qtbot, mocker):
    # Initialize the window instance
    window = Window()
    qtbot.addWidget(window)

    mocker.patch.object(
        window, "create_data_dict", return_value=create_fake_data_dict()
    )

    # Mock the AE instance and association, but allow fill_rtplan to execute
    with patch("pynetdicom.AE") as mock_ae:
        mock_ae_instance = mock_ae.return_value
        mock_assoc = mock_ae_instance.associate.return_value
        mock_assoc.is_established = True

        mock_status = MagicMock()
        mock_status.Status = 0  # Simulate success status
        mock_assoc.send_c_store.return_value = 0

        # Run the send_dicom method, which will use the real fill_rtplan to create rtplan
        window.send_dicom()
        # Verify that send_c_store was actually called
        assert (
            mock_assoc.send_c_store.called
        ), "send_c_store was not called as expected."

        # Extract the rtplan sent to send_c_store if it was called
        if mock_assoc.send_c_store.called:
            args, _ = mock_assoc.send_c_store.call_args
            sent_rtplan = args[0]

            # Verify that all required DICOM fields are present and valid
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
                print(field)
                assert hasattr(sent_rtplan, field), f"{field} is missing in rtplan"

        # Ensure release was called to end the association
        mock_assoc.release.assert_called_once()

        # Check some fields in the generated rtplan
        # assert sent_rtplan.Name == "John"
        # assert sent_rtplan.PatientID == "12345"
        # assert sent_rtplan.Modality == "RTPLAN"
