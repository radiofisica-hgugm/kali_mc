# Configuration File

PREF = 934.70  # Reference Pressure at calibration time (hPa)

DepartmentName = ''

DepartmentLogo_path = r'report/logo_gregoriomaranon.png'

# RECORD AND VERIFY DICOM SERVER SETTINGS ______________________________________________________________________________
destination_server = ''
destination_port = 104
destination_AETitle = ''
PatientSetupLabel = ''

# Tolerances
tol_table_ID = ''
tol_table_label = ''

# Machine
machine = 'LIAC'
serial_number = '0000'
SSD = 645  # mm
# ______________________________________________________________________________________________________________________

# Default path for saving reports
pdf_path = r''

try:
    from local_conf import *
    print("local_conf imported")
except ImportError:
    print("local_conf ignored")
    pass

version = '1.0.0'
