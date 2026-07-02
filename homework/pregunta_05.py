"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    valores_por_letra = {}
    
    # Abrir el archivo en modo lectura
    with open('files\input\data.csv', 'r') as file:
        for linea in file:
            # Eliminar saltos de línea y separar por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Asegurarnos de que la línea tenga los datos necesarios
            if len(columnas) >= 2:
                letra = columnas[0]
                valor = int(columnas[1])
                
                # Si la letra ya está en el diccionario, comparamos los valores
                if letra in valores_por_letra:
                    # Comprobamos si el valor actual es mayor que el máximo guardado (índice 0)
                    if valor > valores_por_letra[letra][0]:
                        valores_por_letra[letra][0] = valor
                        
                    # Comprobamos si el valor actual es menor que el mínimo guardado (índice 1)
                    if valor < valores_por_letra[letra][1]:
                        valores_por_letra[letra][1] = valor
                
                # Si la letra no está, la inicializamos con el valor actual como máximo y mínimo
                else:
                    valores_por_letra[letra] = [valor, valor]
                    
    # Construir la lista de tuplas ordenada alfabéticamente
    resultado = []
    
    # sorted() ordena las claves del diccionario (las letras) alfabéticamente
    for letra in sorted(valores_por_letra.keys()):
        maximo = valores_por_letra[letra][0]
        minimo = valores_por_letra[letra][1]
        # Agregamos la tupla (letra, maximo, minimo) a nuestra lista final
        resultado.append((letra, maximo, minimo))
        
    return resultado
