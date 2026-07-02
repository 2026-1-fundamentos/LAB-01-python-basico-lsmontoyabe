"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    suma_por_letra = {}
    
    # Abrir el archivo en modo lectura
    with open('files\input\data.csv', 'r') as file:
        for linea in file:
            # Eliminar saltos de línea y separar por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Asegurarnos de que la línea tenga al menos dos columnas
            if len(columnas) >= 2:
                letra = columnas[0]
                valor = int(columnas[1]) # Convertimos la segunda columna a entero
                
                # Si la letra ya está en el diccionario, le sumamos el valor
                if letra in suma_por_letra:
                    suma_por_letra[letra] += valor
                # Si no está, la agregamos con el valor inicial
                else:
                    suma_por_letra[letra] = valor
                    
    # Convertir el diccionario a una lista de tuplas y ordenarla alfabéticamente
    resultado = sorted(suma_por_letra.items())
    
    return resultado
