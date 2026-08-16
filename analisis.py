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

def valores_extremos(df, columna):
    """Calcula el valor maximo y minimo de una columna."""
    maximo = df[columna].max()
    minimo = df[columna].min()
    return minimo, maximo

if __name__ == "__main__":
    datos = cargar_datos("diabetes.csv")
    resumen(datos)
    
    # Pruebas de las funciones añadidas
    print("\n--- Analisis de Valores Extremos ---")
    # Nota: Usamos una columna típica de diabetes como 'Age' o 'Glucose'
    try:
        min_val, max_val = valores_extremos(datos, "Age")
        print(f"Edad Minima: {min_val}, Edad Maxima: {max_val}")
    except KeyError:
        print("La columna 'Age' no se encuentra en el dataset.")
# Cambio final para la verificacion del Pull Request del taller
