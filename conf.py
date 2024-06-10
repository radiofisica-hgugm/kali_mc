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
    import local_conf
except ModuleNotFoundError:
    print('local configuration file not found')
