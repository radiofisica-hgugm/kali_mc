# Configuration File

PREF = 934.70  # Reference Pressure at calibration time (hPa)

DepartmentName = ''

DepartmentLogo_path = r'report/logo_gregoriomaranon.png' # The logo should be  25x200 px

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
rescale_factors = False

# Locale:
# By default, fallback to english
locale = 'en'

try:
    from local_conf import *
    print("local_conf imported")
except ImportError:
    print("local_conf ignored")
    pass

version = '1.1.0'


