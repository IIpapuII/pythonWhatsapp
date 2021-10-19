
import pandas as pd
def solicitaRuta():
    ruta = input('Ingrese ruta de DataFrame: ')
    return ruta
def dataFrame(ruta):
    data = pd.read_excel(ruta)
    return data


