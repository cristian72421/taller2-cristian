# analisis.py - Taller 2 Git
import pandas as pd

def cargar_datos(ruta):
    """Carga un archivo CSV en un DataFrame."""
    df = pd.read_csv(ruta)
    return df

def resumen(df):
    """Muestra estadisticas basicas del DataFrame."""
    print("Filas:", df.shape[0])
    print("Columnas:", df.shape[1])
    print(df.describe())

if __name__ == "__main__":
    datos = cargar_datos("BikePrices.csv")
    resumen(datos)