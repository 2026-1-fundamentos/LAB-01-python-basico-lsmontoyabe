"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    suma_por_letra = {}
    
    # Abrir el archivo en modo lectura
    with open('files\input\data.csv', 'r') as file:
        for linea in file:
            # Eliminar saltos de línea y separar por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Asegurarnos de que la línea tenga al menos 4 columnas (índice 3)
            if len(columnas) >= 4:
                # Tomamos el valor de la segunda columna (índice 1) y lo pasamos a entero
                valor = int(columnas[1])
                
                # Tomamos la cuarta columna (índice 3) y separamos sus letras por coma
                letras_col4 = columnas[3].split(',')
                
                # Iteramos sobre cada una de las letras encontradas en esa fila
                for letra in letras_col4:
                    # Si la letra ya está en el diccionario, le sumamos el valor
                    if letra in suma_por_letra:
                        suma_por_letra[letra] += valor
                    # Si no está, la inicializamos con ese valor
                    else:
                        suma_por_letra[letra] = valor
                        
    # Ordenamos el diccionario alfabéticamente por sus claves
    resultado = dict(sorted(suma_por_letra.items()))
    
    return resultado
