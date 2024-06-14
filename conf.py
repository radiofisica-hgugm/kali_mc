# Configuration File

PREF = 934.70  # Reference Pressure at calibration time (hPa)

DepartmentName = ''

# MOSAIQ
destination_server = ''
destination_port = 104
destination_AETitle = ''
PatientSetupLabel = ''

# Tolerancias
tol_table_ID = ''
tol_table_label = ''

# MÁQUINA
machine = 'LIAC'
serial_number = '0000'
SSD = 645 # mm

# Ruta por defecto para informes
pdf_path = r''

try:
    from local_conf import *
    print("local_conf imported")
except ImportError:
    print("local_conf ignored")
    pass

version = '1.0.0'
