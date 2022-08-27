import requests
import random
import json
import time

def obtener_regiones():
    url = "https://restcountries.com/v3.1/all"

    

    response = requests.request("GET", url)
    return response.text

def obtener_pais_por_region(region):
    try:
        url = f"https://restcountries.com/v3.1/region/{region}"
        response = requests.get(url)
        respuesta = json.loads(response.text)
        return respuesta
        
    except Exception as e:
        print(f'ocurrio el error {e}')




if __name__ == '__main__':
    
    
    regiones =  ['Antarctic']
    for region in regiones:
        assert(region)
        start_time = time.time()
        paises = obtener_pais_por_region(region)
        #print(paises)
        try:
            for pais in paises:
                #print(pais['name']['common'])
                print(pais['languages'])
        except Exception as e:
            print('no trae lenguaje')

        #print(len(paises))
