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
    print("Columnas disponibles:", list(df.columns))


def promedio_columna(df, columna):
    """Calcula el promedio de una columna."""
    return df[columna].mean()

def contar_nulos(df):
    """Cuenta los valores nulos por columna."""
    return df.isnull().sum()

if __name__ == "__main__":
    datos = cargar_datos("diabetes.csv")
    resumen(datos)