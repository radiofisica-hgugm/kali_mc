# Configuration File

PREF = 934.70  # Reference Pressure at calibration time (hPa)

# Send to Mosaiq:

# MOSAIQ
destination_server = ''
destination_port = 104
destination_AETitle = ''

# Tolerancias
tol_table_ID = ''
tol_table_label = ''

# MÁQUINA
machine = 'LIAC'

# Ruta por defecto para informes
pdf_path = r''

try:
    from local_conf import *
    print("local_conf imported")
except ImportError:
    print("local_conf ignored")
    pass
