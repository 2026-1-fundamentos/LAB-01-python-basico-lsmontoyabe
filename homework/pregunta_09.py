"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    conteo_claves = {}
    
    # Abrir el archivo en modo lectura
    with open('files\input\data.csv', 'r') as file:
        for linea in file:
            # Eliminar saltos de línea y separar por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Asegurarnos de que la línea tenga al menos 5 columnas
            if len(columnas) >= 5:
                # Tomamos la quinta columna (índice 4)
                diccionario_str = columnas[4]
                
                # Separamos los pares clave-valor por comas
                pares = diccionario_str.split(',')
                
                for par in pares:
                    # Separamos por los dos puntos, pero solo nos interesa el primer elemento (la clave)
                    clave = par.split(':')[0]
                    
                    # Contamos cuántas veces aparece cada clave
                    if clave in conteo_claves:
                        conteo_claves[clave] += 1
                    else:
                        conteo_claves[clave] = 1
                        
    # Para asegurar que el diccionario de salida mantenga el orden alfabético 
    # de las claves (tal como se muestra en la respuesta esperada), lo ordenamos:
    resultado = dict(sorted(conteo_claves.items()))
    
    return resultado
