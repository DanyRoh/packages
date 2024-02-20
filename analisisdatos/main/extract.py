import os.path
import requests
from analisisdatos.main.auxiliar_functions import is_url
import pandas as pd

def extract(path_url, format_file, separator=None):
    """
    Obtiene el archivo de la ruta indicada y lo carga en una variable como un dataframe de Pandas
    :param path: ruta donde se encuentra el archivo
    :param format_file: formato del archivo que se quiere analizar. Formato aceptados: csv, xlsx, xls, txt, html
    :param separator: (Opcional) tipo de separador, en el caso de formatos de archivo que lo requieran
    :return: variable con formato DataFrame de Pandas
    """

    format_accepted = ['csv', 'xlsx', 'xls', 'txt', 'html']
    if format_file not in format_accepted:
        raise Exception('ERROR: Formato de archivo no aceptado. Esta función acepta csv, xlsx, xls, txt o html')

    if is_url(path_url):
        response = requests.get(path_url)
        if not response.status_code == 200:
            raise Exception('ERROR: El archivo no se encuentra en la url especificada')
    else:
        if not os.path.exists(path_url):
            raise Exception('ERROR: El archivo no se encuentra en la ruta especificada')


    load_function = {
        'csv': pd.read_csv,
        'xlsx': pd.read_excel,
        'xls': pd.read_excel,
        'txt': lambda path_txt, sep: pd.read_csv(path_txt, sep=sep),
        'html': pd.read_html
    }

    if format_file == 'txt':
        df = load_function[format_file](path_url, separator)
    else:
        df = load_function[format_file](path_url)

    return df
