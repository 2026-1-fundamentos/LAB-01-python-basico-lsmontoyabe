"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    conteo = {}
    
    # Abrir el archivo en modo lectura
    with open('files\input\data.csv', 'r') as file:
        for linea in file:
            # Eliminar saltos de línea y separar por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Asegurarnos de que la línea no esté vacía
            if len(columnas) > 0:
                letra = columnas[0]
                
                # Si la letra ya está en el diccionario, sumamos 1
                if letra in conteo:
                    conteo[letra] += 1
                # Si no está, la agregamos con valor inicial de 1
                else:
                    conteo[letra] = 1
                    
    # Convertir el diccionario a una lista de tuplas y ordenarla alfabéticamente
    resultado = sorted(conteo.items())
    
    return resultado
