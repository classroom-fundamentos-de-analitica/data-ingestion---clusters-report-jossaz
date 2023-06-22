"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


import re
def ingest_data():
  # Leer el archivo de texto
  with open('clusters_report.txt', 'r') as file:
      lines = file.readlines()
  
  # Definir patrón de expresiones regulares para analizar cada línea
  pattern = r"\s+(\d+)\s+(\d+)\s+([\d,\.]+%)\s+(.+)"
  
  # Extraer los datos de cada línea y crear una lista de diccionarios
  data = []
  for line in lines[5:]:
      line = line.strip()
      if line:
          match = re.match(pattern, line)
          if match:
              cluster = int(match.group(1))
              cantidad = int(match.group(2))
              porcentaje = float(match.group(3).rstrip('%').replace(',', '.'))
              palabras_clave = match.group(4).replace('-', '').replace('  ', ', ')
              data.append({
                  'cluster': cluster,
                  'cantidad_de_palabras_clave': cantidad,
                  'porcentaje_de_palabras_clave': porcentaje,
                  'principales_palabras_clave': palabras_clave
              })
  
  # Crear el dataframe de Pandas
  df = pd.DataFrame(data)
  return df
