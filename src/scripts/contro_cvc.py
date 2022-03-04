
import pandas as pd
"""
    Esta funcion busca traer la ruta espesifica del archivo  de
    ubicación de data frama a importar con los numero a intervenir.
    """
def solicitaRuta():
    ruta = input('Ingrese ruta de DataFrame: ')
    return ruta
def dataFrame(ruta):
    data = pd.read_excel(ruta)
    return data
