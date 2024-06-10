from report_utils import create_pdf
import datetime
import os


def create_fake_data_dict():
    data_dict = {
        'Name': 'Gustave',
        'Surname': 'Flaubert',
        'ID': '3456734',
        'Site': 'Sarcoma Retroperitoneal',
        'Physicist': 'Luis de Góngora y Argote',
        'Oncologist': 'Honoré de Balzac',
        'TERt': 'Victor Hugo, Francisco de Quevedo y Villegas',
        'Date': f'{datetime.date.today().strftime("%d-%m-%Y")}',

        'Applicator': '10',
        'Bevel': '45',
        'Dose': '1250',

        'Energy': 10,
        'Output': 1.1,
        'UM': 2500,

        'Pitch': '3',
        'Roll': '10',
        'Vertical': '220',

        'IORT_number': '2999',

        'Comments': 'No habido problemas con la irradiación, Si la línea es muy larga es posible que se salga de el recuadro.'
    }
    return data_dict


os.chdir('..')
data_dict = create_fake_data_dict()
create_pdf('test/report_test.pdf', 'test/cross.png', 'test/in.png','test/3D.png', data_dict)