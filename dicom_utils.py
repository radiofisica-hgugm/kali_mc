# ENVÍO DE DATOS A SERVIDOR DICOM
from pydicom import dcmread
from pydicom.uid import ImplicitVRLittleEndian

from pynetdicom import AE, VerificationPresentationContexts
from pynetdicom.sop_class import CTImageStorage, RTStructureSetStorage, RTPlanStorage
import random
import datetime
import os
import conf


def generate_uid(prefix='1.2.392.200036.9116.2.6.1.48.'):
    uid = prefix + str(random.randint(1e10,1e12))
    return uid


def send_rtplan(data_dict):
    # TODO: remove dicom file and code all fields
    rtplan = dcmread(os.path.join('dcm', 'test.dcm'), force=True)
    rtplan.file_meta.TransferSyntaxUID = ImplicitVRLittleEndian

    StudyUID = generate_uid()
    SeriesUID = generate_uid()

    rtplan.SOPInstanceUID = generate_uid()
    rtplan.StudyInstanceUID = StudyUID
    rtplan.SeriesInstanceUID = SeriesUID
    today = datetime.date.today()
    rtplan.RTPlanDate = today
    rtplan.StudyDate = today
    rtplan.SeriesDate = today
    rtplan.StudyDescription = 'IORT'


    rtplan.PatientName = data_dict['Surname']
    rtplan.OtherPatientNames = data_dict['Name']
    rtplan.PatientID = data_dict['ID']
    rtplan.OtherPatientIDs = data_dict['ID']
    rtplan.ManufacturerModelName = 'Kali MC'
    rtplan.Manufacturer = 'HGUGM'
    rtplan.SoftwareVersions = conf.version
    rtplan.RTPlanLabel = f"RIO_N{data_dict['IORT_number']}"
    rtplan.RTPlanName = f"RIO_N{data_dict['IORT_number']}"

    # Prescripción
    rtplan.DoseReferenceSequence[0].TargetPrescriptionDose = float(data_dict['Dose']) / 100  # en Gy
    rtplan.DoseReferenceSequence[0].DoseReferenceDescription = data_dict['Site']
    rtplan.DoseReferenceSequence[0].DoseReferencePointCoordinates = [0.0, -float(data_dict['R90']), 0.0]
    rtplan.ToleranceTableSequence[0].ToleranceTableNumber = conf.tol_table_ID
    rtplan.ToleranceTableSequence[0].ToleranceTableLabel = conf.tol_table_label

    # CONF SITIO
    rtplan.PatientSetupSequence[0].PatientSetupLabel = conf.PatientSetupLabel

    # Beam
    rtplan.BeamSequence[0].InstitutionalDepartmentName = conf.DepartmentName
    rtplan.BeamSequence[0].TreatmentMachineName = conf.machine
    rtplan.BeamSequence[0].ApplicatorSequence[0].ApplicatorID = f"C{data_dict['Applicator']}B{data_dict['Bevel']}"
    rtplan.FractionGroupSequence[0].ReferencedBeamSequence[0].BeamMeterset = int(data_dict['UM'])  # UM
    rtplan.FractionGroupSequence[0].ReferencedBeamSequence[0].BeamDose = float(data_dict['Dose']) / 100
    rtplan.BeamSequence[0].ControlPointSequence[0].NominalBeamEnergy= int(data_dict['Energy'])
    app_diam= float(data_dict['Applicator'])
    rtplan.BeamSequence[0].ControlPointSequence[0].BeamLimitingDevicePositionSequence[0].LeafJawPositions = [-app_diam/2 * 10, app_diam/2 * 10]
    rtplan.BeamSequence[0].ControlPointSequence[0].BeamLimitingDevicePositionSequence[1].LeafJawPositions = [-app_diam/2 * 10, app_diam/2 * 10]
    rtplan.BeamSequence[0].ControlPointSequence[0].SourceToSurfaceDistance = conf.SSD

    print('Asociación con servidor remoto ..............')
    ae = AE(ae_title='MY_STORAGE_SCU')
    # We can also do the same thing with the requested contexts
    ae.requested_contexts = VerificationPresentationContexts
    # Or we can use inbuilt objects like CTImageStorage.
    # The requested presentation context's transfer syntaxes can also
    #   be specified using a str/UID or list of str/UIDs
    ae.add_requested_context(CTImageStorage,
                             transfer_syntax=ImplicitVRLittleEndian)
    ae.add_requested_context(RTStructureSetStorage,
                             transfer_syntax=ImplicitVRLittleEndian)
    ae.add_requested_context(RTPlanStorage,
                             transfer_syntax=ImplicitVRLittleEndian)

    assoc = ae.associate(conf.destination_server, conf.destination_port, ae_title=conf.destination_AETitle)

    if assoc.is_established:
        print('Enviando archivos DICOM a servidor remoto ......................')
        status = assoc.send_c_store(rtplan)
        if status.Status != 0:
            print('Error en la transferencia!')
        else:
            print('DICOM RTPlan enviado con éxito')

        assoc.release()
