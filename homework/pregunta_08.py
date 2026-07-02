"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

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
                
                # Usar un set (conjunto) para evitar letras duplicadas automáticamente
                if numero in agrupacion_por_numero:
                    agrupacion_por_numero[numero].add(letra)
                else:
                    # Inicializamos el valor como un conjunto con una sola letra
                    agrupacion_por_numero[numero] = {letra}
                    
    # Construir la lista de resultados
    resultado = []
    
    # Ordenar los números (claves del diccionario)
    for numero in sorted(agrupacion_por_numero.keys()):
        # sorted() toma el conjunto, lo ordena alfabéticamente y lo devuelve como una lista
        letras_ordenadas_sin_repetir = sorted(agrupacion_por_numero[numero])
        
        # Agregamos la tupla a nuestra lista final
        resultado.append((numero, letras_ordenadas_sin_repetir))
        
    return resultado
