# ENVÍO DE DATOS A SERVIDOR DICOM
from pydicom import dcmread
from pydicom import Sequence, Dataset
from pydicom.uid import ImplicitVRLittleEndian
from pydicom.dataset import FileDataset, FileMetaDataset
from pydicom.uid import UID

from pynetdicom import AE, VerificationPresentationContexts
from pynetdicom.sop_class import CTImageStorage, RTStructureSetStorage, RTPlanStorage
import random
import datetime
import tempfile
import os
import conf


def generate_uid(prefix="1.2.392.200036.9116.2.6.1.48."):
    uid = prefix + str(random.randint(1e10, 1e12))
    return uid


def send_rtplan(data_dict):
    rtplan_meta = FileMetaDataset()

    with tempfile.TemporaryFile() as fp:
        rtplan = FileDataset(fp, {}, file_meta=rtplan_meta, preamble=b"\0" * 128)

        rtplan.file_meta.TransferSyntaxUID = ImplicitVRLittleEndian
        rtplan.SOPClassUID = UID(
            "1.2.840.10008.5.1.4.1.1.481.5"
        )  # SOP Class: RT Plan Storage

        rtplan.Modality = "RTPLAN"
        rtplan.PrescriptionDescription = f"IORT Nº: {data_dict['IORT_number']}"
        rtplan.PlanIntent = "CURATIVE"
        rtplan.ApprovalStatus = "UNAPPROVED"
        rtplan.RTPlanGeometry = "TREATMENT_DEVICE"

        StudyUID = generate_uid()
        SeriesUID = generate_uid()

        rtplan.SOPInstanceUID = generate_uid()
        rtplan.StudyInstanceUID = StudyUID
        rtplan.SeriesInstanceUID = SeriesUID
        today = datetime.date.today()
        rtplan.RTPlanDate = today
        rtplan.RTPlanTime = datetime.datetime.now().time()
        rtplan.StudyDate = today
        rtplan.SeriesDate = today
        rtplan.StudyDescription = "IORT"

        rtplan.PatientName = data_dict["Surname"]
        rtplan.OtherPatientNames = data_dict["Name"]
        rtplan.PatientID = data_dict["ID"]
        rtplan.OtherPatientIDs = data_dict["ID"]
        rtplan.ManufacturerModelName = "Kali MC"
        rtplan.Manufacturer = "HGUGM"
        rtplan.SoftwareVersions = conf.version
        rtplan.RTPlanLabel = f"01_IORT_N{data_dict['IORT_number']}"
        rtplan.RTPlanName = f"01_IORT_N{data_dict['IORT_number']}"

        # Prescription
        rtplan.DoseReferenceSequence = Sequence([Dataset()])
        rtplan.DoseReferenceSequence[0].DoseReferenceNumber = "1"
        rtplan.DoseReferenceSequence[0].DoseReferenceType = "TARGET"
        rtplan.DoseReferenceSequence[0].DoseReferenceStructureType = "SITE"
        rtplan.DoseReferenceSequence[0].TargetPrescriptionDose = (
            float(data_dict["Dose"]) / 100
        )  # en Gy
        rtplan.DoseReferenceSequence[0].DoseReferenceDescription = data_dict["Site"]
        rtplan.DoseReferenceSequence[0].DoseReferencePointCoordinates = [
            0.0,
            -float(data_dict["R90"]),
            0.0,
        ]

        rtplan.ToleranceTableSequence = Sequence([Dataset()])
        rtplan.ToleranceTableSequence[0].ToleranceTableNumber = conf.tol_table_ID
        rtplan.ToleranceTableSequence[0].ToleranceTableLabel = conf.tol_table_label

        # Site configuration
        rtplan.PatientSetupSequence = Sequence([Dataset()])
        rtplan.PatientSetupSequence[0].PatientSetupNumber = "1"
        rtplan.PatientSetupSequence[0].PatientPosition = "HFS"  # Not relevant
        rtplan.PatientSetupSequence[0].SetupTechnique = "FIXED_SSD"
        rtplan.PatientSetupSequence[0].PatientSetupLabel = conf.PatientSetupLabel

        # Beam
        rtplan.BeamSequence = Sequence([Dataset()])
        rtplan.BeamSequence[0].BeamNumber = "1"
        rtplan.BeamSequence[0].BeamType = "STATIC"
        rtplan.BeamSequence[0].RadiationType = "ELECTRON"
        rtplan.BeamSequence[0].TreatmentDeliveryType = "TREATMENT"
        rtplan.BeamSequence[0].BeamName = "IORT"
        rtplan.BeamSequence[0].BeamDescription = "IORT BEAM"
        rtplan.BeamSequence[0].NumberOfWedges = "0"
        rtplan.BeamSequence[0].NumberOfCompensators = "0"
        rtplan.BeamSequence[0].NumberOfBoli = "0"
        rtplan.BeamSequence[0].NumberOfBlocks = "0"

        rtplan.BeamSequence[0].InstitutionalDepartmentName = conf.DepartmentName
        rtplan.BeamSequence[0].TreatmentMachineName = conf.machine
        rtplan.BeamSequence[0].PrimaryDosimeterUnit = "MU"

        rtplan.BeamSequence[0].ApplicatorSequence = Sequence([Dataset()])
        rtplan.BeamSequence[0].ApplicatorSequence[
            0
        ].ApplicatorID = f"C{data_dict['Applicator']}B{data_dict['Bevel']}"
        rtplan.BeamSequence[0].ApplicatorSequence[0].ApplicatorType = "INTRAOPERATIVE"
        rtplan.BeamSequence[0].ApplicatorSequence[
            0
        ].ApplicatorDescription = f"C{data_dict['Applicator']}B{data_dict['Bevel']}"

        rtplan.FractionGroupSequence = Sequence([Dataset()])
        rtplan.FractionGroupSequence[0].FractionGroupNumber = "1"
        rtplan.FractionGroupSequence[0].NumberOfFractionsPlanned = "1"
        rtplan.FractionGroupSequence[0].NumberOfBeams = "1"
        rtplan.FractionGroupSequence[0].NumberOfBrachyApplicationSetups = "0"
        rtplan.FractionGroupSequence[0].ReferencedBeamSequence = Sequence([Dataset()])
        rtplan.FractionGroupSequence[0].ReferencedBeamSequence[
            0
        ].ReferencedBeamNumber = "1"
        rtplan.FractionGroupSequence[0].ReferencedBeamSequence[0].BeamMeterset = int(
            data_dict["UM"]
        )  # UM
        rtplan.FractionGroupSequence[0].ReferencedBeamSequence[0].BeamDose = (
            float(data_dict["Dose"]) / 100
        )
        rtplan.FractionGroupSequence[0].ReferencedBeamSequence[
            0
        ].BeamDoseSpecificationPoint = [0.0, 0.0, 0.0]
        rtplan.FractionGroupSequence[0].ReferencedDoseReferenceSequence = Sequence(
            [Dataset()]
        )
        rtplan.FractionGroupSequence[0].ReferencedDoseReferenceSequence[
            0
        ].ReferencedDoseReferenceNumber = "1"

        rtplan.BeamSequence[0].ControlPointSequence = Sequence([Dataset()])
        rtplan.BeamSequence[0].ControlPointSequence[0].ControlPointIndex = "0"
        rtplan.BeamSequence[0].ControlPointSequence[0].NominalBeamEnergy = int(
            data_dict["Energy"]
        )
        rtplan.BeamSequence[0].ControlPointSequence[0].GantryAngle = data_dict["Roll"]
        rtplan.BeamSequence[0].ControlPointSequence[0].GantryRotationDirection = "CW"
        rtplan.BeamSequence[0].ControlPointSequence[0].BeamLimitingDeviceAngle = 0.0
        rtplan.BeamSequence[0].ControlPointSequence[
            0
        ].BeamLimitingDeviceRotationDirection = "CW"
        rtplan.BeamSequence[0].ControlPointSequence[0].PatientSupportAngle = 0.0
        rtplan.BeamSequence[0].ControlPointSequence[
            0
        ].PatientSupportRotationDirection = "CW"
        rtplan.BeamSequence[0].ControlPointSequence[0].TableTopVerticalPosition = "0.0"
        rtplan.BeamSequence[0].ControlPointSequence[0].TableTopEccentricAngle = 0.0
        rtplan.BeamSequence[0].ControlPointSequence[0].TableTopPitchAngle = 0.0
        rtplan.BeamSequence[0].ControlPointSequence[0].TableTopRollAngle = 0.0
        rtplan.BeamSequence[0].ControlPointSequence[0].GantryPitchAngle = data_dict[
            "Pitch"
        ]
        rtplan.BeamSequence[0].ControlPointSequence[
            0
        ].GantryPitchRotationDirection = "CW"
        rtplan.BeamSequence[0].ControlPointSequence[0].IsocenterPosition = [
            0.0,
            0.0,
            0.0,
        ]

        app_diam = float(data_dict["Applicator"])
        rtplan.BeamSequence[0].ControlPointSequence[
            0
        ].BeamLimitingDevicePositionSequence = Sequence([Dataset(), Dataset()])
        rtplan.BeamSequence[0].ControlPointSequence[
            0
        ].BeamLimitingDevicePositionSequence[0].RTBeamLimitingDeviceType = "ASYMX"
        rtplan.BeamSequence[0].ControlPointSequence[
            0
        ].BeamLimitingDevicePositionSequence[0].LeafJawPositions = [
            -app_diam / 2 * 10,
            app_diam / 2 * 10,
        ]
        rtplan.BeamSequence[0].ControlPointSequence[
            0
        ].BeamLimitingDevicePositionSequence[1].RTBeamLimitingDeviceType = "ASYMY"
        rtplan.BeamSequence[0].ControlPointSequence[
            0
        ].BeamLimitingDevicePositionSequence[1].LeafJawPositions = [
            -app_diam / 2 * 10,
            app_diam / 2 * 10,
        ]

        rtplan.BeamSequence[0].ControlPointSequence[
            0
        ].SourceToSurfaceDistance = conf.SSD
        rtplan.BeamSequence[0].ReferencedPatientSetupNumber = "1"
        rtplan.BeamSequence[0].ReferencedToleranceTableNumber = "1"

        print("Associating with remote DICOM server ..............")
        ae = AE(ae_title="MY_STORAGE_SCU")
        # We can also do the same thing with the requested contexts
        ae.requested_contexts = VerificationPresentationContexts
        # Or we can use inbuilt objects like CTImageStorage.
        # The requested presentation context's transfer syntaxes can also
        #   be specified using a str/UID or list of str/UIDs
        ae.add_requested_context(CTImageStorage, transfer_syntax=ImplicitVRLittleEndian)
        ae.add_requested_context(
            RTStructureSetStorage, transfer_syntax=ImplicitVRLittleEndian
        )
        ae.add_requested_context(RTPlanStorage, transfer_syntax=ImplicitVRLittleEndian)

        assoc = ae.associate(
            conf.destination_server,
            conf.destination_port,
            ae_title=conf.destination_AETitle,
        )

        if assoc.is_established:
            print("Sending DICOM file to remote server ......................")
            status = assoc.send_c_store(rtplan)
            if status.Status != 0:
                print("Tranfer error!")
            else:
                print("DICOM RTPlan was successfully sent")

            assoc.release()
