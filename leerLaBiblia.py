import  json
import re





with open('es_rvr.json', 'r', encoding='UTF-8') as file:
    data =  json.load(file)


def existePalabraEnCapitulosAvanzado(palabra):
    contador=0
    versiculosEncontrados=[]
    contadorPalabrasEncontradas=[]
    palabra = palabra.lower()
    for libro in  data:
        contadorCapitulo=0
        for capitulos in libro['chapters']:
            contadorVersiculo=0
            contadorCapitulo+=1
            for versiculo in capitulos:
                contadorVersiculo+=1
                versiculo = versiculo.lower()
                encontradas = re.findall(r'\b' + palabra + r'\b', versiculo)
                if  encontradas !=  []:
                    contadorPalabrasEncontradas = len(encontradas)
                    contador+=contadorPalabrasEncontradas
                    versiculosEncontrados.append(libro['name']+f' {contadorCapitulo}:{contadorVersiculo}')
    if contador != 0:
        versiculosEncontrados = list(dict.fromkeys(versiculosEncontrados))
        return True, contador, versiculosEncontrados                
    return False, contador, versiculosEncontrados

def existePalabraEnCapitulos(palabra):
    contador=0
    librosEncontrados=[]
    contadorPalabrasEncontradas=[]
    palabra = palabra.lower()
    for libro in  data:
        for capitulos in libro['chapters']:
            for versiculo in capitulos:
                versiculo = versiculo.lower()
                encontradas = re.findall(r'\b' + palabra + r'\b', versiculo)
                if  encontradas !=  []:
                    contadorPalabrasEncontradas = len(encontradas)
                    contador+=contadorPalabrasEncontradas
                    librosEncontrados.append(libro['name'])
    if contador != 0:
        librosEncontrados = list(dict.fromkeys(librosEncontrados))
        return True, contador, librosEncontrados                
    return False, contador, librosEncontrados

def conseguirNombreDeLibros(listaDeLibros):
    contador = 0
    finContador = len(listaDeLibros)
    textoConNombres='' 
    for nombre in listaDeLibros:
        contador+=1
        if contador== finContador:
            textoConNombres=textoConNombres+nombre
        elif contador== (finContador-1):
            textoConNombres=textoConNombres+nombre+' y '
        else:
            textoConNombres=textoConNombres+nombre +', '
    textoConNombres.strip()
    return textoConNombres

# existe, cantidad,librosEncontrados = existePalabraEnCapitulos('jesus')
# lista = conseguirNombreDeLibros(librosEncontrados)
# print(lista)
