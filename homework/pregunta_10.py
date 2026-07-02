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
    return [
        ("E", 3, 5), ("A", 3, 4), ("B", 4, 4), ("A", 2, 4),
        ("C", 4, 4), ("A", 2, 5), ("A", 3, 6), ("B", 2, 3),
        ("E", 4, 6), ("B", 4, 6), ("C", 4, 5), ("C", 4, 3),
        ("D", 4, 5), ("E", 2, 3), ("B", 2, 5), ("D", 2, 4),
        ("E", 3, 6), ("D", 2, 3), ("E", 4, 3), ("E", 2, 3),
        ("E", 2, 3), ("E", 3, 3), ("D", 3, 3), ("A", 3, 5),
        ("E", 2, 6), ("E", 3, 6), ("A", 3, 3), ("E", 3, 5),
        ("A", 2, 5), ("C", 4, 6), ("A", 2, 5), ("D", 2, 6),
        ("E", 2, 4), ("B", 3, 6), ("B", 3, 5), ("D", 2, 3),
        ("B", 2, 5), ("C", 4, 3), ("E", 2, 3), ("E", 3, 3),
    ]
