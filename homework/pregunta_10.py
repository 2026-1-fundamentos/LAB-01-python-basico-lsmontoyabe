"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    resultado = []
    
    # Abrir el archivo en modo lectura
    with open('files\input\data.csv', 'r') as file:
        for linea in file:
            # Eliminar saltos de línea y separar por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Asegurarnos de que la línea tenga al menos 5 columnas
            if len(columnas) >= 5:
                letra = columnas[0]
                
                # La cuarta columna (índice 3) tiene letras separadas por comas
                # Separamos por coma y contamos el tamaño de la lista resultante con len()
                cantidad_col4 = len(columnas[3].split(','))
                
                # La quinta columna (índice 4) tiene diccionarios separados por comas
                # Hacemos lo mismo: separamos por coma y contamos
                cantidad_col5 = len(columnas[4].split(','))
                
                # Agregamos la tupla con los tres datos solicitados
                resultado.append((letra, cantidad_col4, cantidad_col5))
                
    return resultado
