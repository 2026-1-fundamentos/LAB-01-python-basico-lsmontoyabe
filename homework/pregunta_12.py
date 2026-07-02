"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_por_letra = {}
    
    # Abrir el archivo en modo lectura
    with open('files\input\data.csv', 'r') as file:
        for linea in file:
            # Eliminar saltos de línea y separar por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Asegurarnos de que la línea tenga al menos 5 columnas
            if len(columnas) >= 5:
                letra = columnas[0]
                
                # Tomamos la quinta columna y separamos sus pares
                pares = columnas[4].split(',')
                
                # Variable para acumular la suma de los valores numéricos de esta fila
                suma_fila = 0
                for par in pares:
                    # Separamos por ':' y tomamos el segundo elemento (el número)
                    valor_str = par.split(':')[1]
                    suma_fila += int(valor_str)
                    
                # Acumulamos el resultado en nuestro diccionario principal
                if letra in suma_por_letra:
                    suma_por_letra[letra] += suma_fila
                else:
                    suma_por_letra[letra] = suma_fila
                    
    # Ordenamos el diccionario alfabéticamente por la clave (la letra)
    resultado = dict(sorted(suma_por_letra.items()))
    
    return resultado
