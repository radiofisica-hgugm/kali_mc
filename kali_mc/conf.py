# Configuration File

PREF = 934.70
"""
Reference Pressure at calibration time (hPa).

WARNING! This affects the Monitor Units calculation!
"""

DepartmentName = ""
"""
The name of the department, this will show in the generated report.
"""

DepartmentLogo_path = (
    r"report/logo_gregoriomaranon.png"  # The logo should be  25x200 px
)
"""
The path to the logo of the institution/department. This will show in the generated report.
"""

"""
RECORD AND VERIFY DICOM SERVER SETTINGS
"""
destination_server = "mosaiq.yourinstitution.org"
"""
IP or Hostname of the Record & Verify server
e.g. 192.168.1.10
"""
destination_port = 104
"""
Port of the destination Record & Verify server, defaults to 104.
"""
destination_AETitle = "IMPAC_DCM_SCP"
"""
The AETitle of the destination Record & Verify server.
Mosaiq uses 'IMPAC_DCM_SCP'
"""
PatientSetupLabel = ""
"""
DICOM PatientSetupLabel, this is mapped in MOSAIQ when importing the plan.
"""

# Tolerances
tol_table_ID = ""
"""
The ID of the Tolerance table to be DICOM exported to the Record & Verify system.
"""
tol_table_label = ""
"""
The label of the Tolerance table to be DICOM exported to the Record & Verify system.
"""

# Machine
machine = "LIAC HWL"
"""
The name or model of your linac. This will show in the generated report.
"""
serial_number = "0000"
"""
The serial number of your linac. This will show in the generated report.
"""

SSD = 645  # mm

# ______________________________________________________________________________________________________________________

# Default path for saving reports
pdf_path = r""
"""
The default path to save the generated reports. It can be a UNC path.
"""
rescale_factors = False
"""
Whether to apply rescaling factors to some absorbed dose distributions.
"""


# Locale:
# By default, fallback to english
locale = "en"
"""
Default language. Available choices are 'es_ES' or 'en' [DEFAULT].
"""

try:
    from local_conf import *

    print("local_conf imported")
except ImportError:
    print("local_conf ignored")
    pass

__version__ = "1.2.0"
