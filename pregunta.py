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

# Leer el archivo de informe de clústeres
def ingest_data():
  with open('clusters_report.txt', 'r') as file:
      lines = file.readlines()
  
  # Patrón de expresión regular para extraer los datos
  pattern = r'\s+(\d+)\s+(\d+)\s+([\d,.\s]+%)\s+(.*)'
  
  # Extraer los datos de cada línea del archivo
  data = []
  for line in lines[2:]:
      match = re.search(pattern, line)
      if match:
          cluster = int(match.group(1))
          cantidad = int(match.group(2))
          porcentaje = float(match.group(3).replace(',', '.').replace(' %', ''))
          palabras_clave = match.group(4)
          
          # Realizar los ajustes en el formato de las palabras clave
          palabras_clave = palabras_clave.replace('  ', '').replace(', ', ',').replace(',',', ')
          
          data.append([cluster, cantidad, porcentaje, palabras_clave])
  
  # Crear el DataFrame
  df = pd.DataFrame(data, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])
  return df
