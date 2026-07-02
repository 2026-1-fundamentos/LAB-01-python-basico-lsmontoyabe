"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    valores_por_clave = {}
    
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
                    # Separamos la clave y el valor por los dos puntos
                    clave, valor_str = par.split(':')
                    valor = int(valor_str)
                    
                    # Lógica para encontrar el mínimo y el máximo
                    if clave in valores_por_clave:
                        # Comparar y actualizar el mínimo (índice 0)
                        if valor < valores_por_clave[clave][0]:
                            valores_por_clave[clave][0] = valor
                        
                        # Comparar y actualizar el máximo (índice 1)
                        if valor > valores_por_clave[clave][1]:
                            valores_por_clave[clave][1] = valor
                    else:
                        # Si es la primera vez que vemos la clave, inicializamos [min, max]
                        valores_por_clave[clave] = [valor, valor]
                        
    # Construir la lista de tuplas ordenada alfabéticamente
    resultado = []
    
    for clave in sorted(valores_por_clave.keys()):
        minimo = valores_por_clave[clave][0]
        maximo = valores_por_clave[clave][1]
        resultado.append((clave, minimo, maximo))
        
    return resultado
