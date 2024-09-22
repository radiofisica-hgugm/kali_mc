import datetime
import os

from report_utils import create_pdf


def create_fake_data_dict():
    data_dict = {
        "Name": "Gustave",
        "Surname": "Flaubert",
        "ID": "3456734",
        "Site": "Sarcoma Retroperitoneal",
        "Physicist": "Luis de Góngora y Argote",
        "Oncologist": "Honoré de Balzac",
        "TERt": "Victor Hugo, Francisco de Quevedo y Villegas",
        "Date": f'{datetime.date.today().strftime("%d-%m-%Y")}',
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
        "Pitch": "3",
        "Roll": "10",
        "Vertical": "220",
        "IORT_number": "2999",
        "Comments": "No habido problemas con la irradiación, Si la línea es muy larga es posible que "
        "se salga del recuadro. Un poco más de información para ver cómo se rellena",
    }
    return data_dict


filepath = os.path.dirname(__file__)
data_dict = create_fake_data_dict()
create_pdf(
    os.path.join(filepath, "report_test.pdf"),
    os.path.join(filepath, "cross.png"),
    os.path.join(filepath, "in.png"),
    os.path.join(filepath, "coronal.png"),
    os.path.join(filepath, "3D.png"),
    data_dict,
)
