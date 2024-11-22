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

# External data
enable_external_data = False
"""
Whether to use external data for MU calculations and R90 values. A valid path is needed in `external_data_path`
"""

external_data_path = r""
"""
A valid path to external data files in numpy format, please check the docs for details. Only takes effect if
`enable_external_data == True`.
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

__version__ = "1.3.0"

# Data files to check for integrity
applicators = [3, 4, 5, 6, 7, 8, 9, 10, 12]
bevels = [0, 15, 30, 45]
energies = [6, 8, 10, 12]
# OFs
datafiles_list = [f"OF_C{i}.npz" for i in applicators]
# R90s
[datafiles_list.append(f"R90_C{i}.npz") for i in applicators]
datafiles_list.append("rescaling_factors.npy")
datafiles_list.append("sim/OFs_penEasy.npz")
datafiles_list.append("sim/R90s_penEasy.npz")

for d in applicators:
    for b in bevels:
        for en in energies:
            datafiles_list.append(f"sim/C{d}/B{b}/C{d}B{b}_{en}MeV.npz")
