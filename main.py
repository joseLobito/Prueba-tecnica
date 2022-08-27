import pandas as pd
import time 
import hashlib

from helpers.consumo_api import *
from helpers.BaseDatos import *

data = pd.read_json(obtener_regiones())
regiones = data["region"].value_counts().keys().to_list()


bd = []
for region in regiones:
    assert(region)
    start_time = time.time()
    paises = obtener_pais_por_region(region)
    try:
        for pais in paises:
            start_time = time.time()
            
            
            assert(pais['languages'])
            
            
            
            for clave,valor in pais['languages'].items():

                
                valor = hashlib.sha1(valor.encode('UTF-8')).hexdigest()
                
                
                bd.append([region,pais['name']['common'],valor, time.time()-start_time])
            
    except Exception as e:
        
        print("no tiene lenguaje")

dataframe = pd.DataFrame(bd, columns=["Region", "Country", "Language","Time"])
print(dataframe)
print(f"Tiempo total: {dataframe['Time'].sum()} s")
print(f"Tiempo promedio: {dataframe['Time'].mean()} s")
print(f"Tiempo minimo: {dataframe['Time'].min()} s")
print(f"Tiempo maximo: {dataframe['Time'].max()} s")

base_datos = MetodosBD()
base_datos.crear_tabla()
for i in bd:
    base_datos.insertar_datos(i)
for i in base_datos.mostrar_datos():
    print(i)

dataframe.to_json('json/data.json')

print('--------- Dataframe from data.json ----------')
print(pd.read_json('json/data.json'))