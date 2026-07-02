"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    agrupacion_por_numero = {}
    
    # Abrir el archivo en modo lectura
    with open('files\input\data.csv', 'r') as file:
        for linea in file:
            # Eliminar saltos de línea y separar por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Asegurarnos de que la línea tenga al menos dos columnas
            if len(columnas) >= 2:
                letra = columnas[0]
                numero = int(columnas[1])
                
                # Si el número ya existe como clave, agregamos la letra a su lista
                if numero in agrupacion_por_numero:
                    agrupacion_por_numero[numero].append(letra)
                # Si el número no existe, creamos la clave e inicializamos la lista con la letra
                else:
                    agrupacion_por_numero[numero] = [letra]
                    
    # sorted() ordenará el diccionario basándose en las claves (los números) de menor a mayor
    # .items() convierte el diccionario en una lista de tuplas (numero, lista_letras)
    resultado = sorted(agrupacion_por_numero.items())
    
    return resultado
