"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    with open('clusters_report.txt', 'r') as file:
    content = file.read()

# Procesar los datos
lines = content.split('\n')
data = []
for line in lines:
    line = line.strip()
    if line.startswith('Cluster') or line == '':
        continue
    elements = line.split()
    cluster = {
        'cluster': int(elements[0]),
        'cantidad_de_palabras_clave': int(elements[1]),
        'porcentaje_de_palabras_clave': float(elements[2].replace('%', '').replace(',', '.')),
        'palabras_clave': ', '.join(elements[3:])
    }
    data.append(cluster)

# Crear el DataFrame
df = pd.DataFrame(data)

# Reemplazar espacios por guiones bajos en los nombres de las columnas
df.columns = df.columns.str.replace(' ', '_').str.lower()

# Mostrar el DataFrame resultante
print(df)

    return df
