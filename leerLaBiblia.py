import  json
import re


with open('es_rvr.json', 'r', encoding='UTF-8') as file:
    data =  json.load(file)



libro = [dictonary['chapters']  for dictonary in  data]

def existePalabraEnCapitulos(palabra):
    contador=0
    contadorPalabrasEncontradas=[]
    palabra = palabra.lower()
    for capitulos in  libro:
        for capitulo in capitulos:
            for versiculo in capitulo:
                versiculoNormalizado = versiculo.lower()
                encontradas = re.findall(r'\b' + palabra + r'\b', versiculoNormalizado)
                if  encontradas !=  None:
                    contadorPalabrasEncontradas = len(encontradas)
                    contador+=contadorPalabrasEncontradas
    if contador != 0:
        return True, contador                
    return False, 0


existe, cantidad = existePalabraEnCapitulos('uyvuyvuyv')
print(existe)