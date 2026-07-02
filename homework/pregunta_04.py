"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    conteo_meses = {}
    
    # Abrir el archivo en modo lectura
    with open('files\input\data.csv', 'r') as file:
        for linea in file:
            # Eliminar saltos de línea y separar por tabulaciones
            columnas = linea.strip().split('\t')
            
            # Asegurarnos de que la línea tenga al menos tres columnas
            if len(columnas) >= 3:
                # La tercera columna contiene la fecha
                fecha = columnas[2] 
                
                # Separamos la fecha por los guiones y tomamos el segundo elemento (el mes)
                # Ejemplo: '1999-02-28'.split('-') produce ['1999', '02', '28']
                mes = fecha.split('-')[1]
                
                # Si el mes ya está en el diccionario, sumamos 1 al contador
                if mes in conteo_meses:
                    conteo_meses[mes] += 1
                # Si no está, lo agregamos con un valor inicial de 1
                else:
                    conteo_meses[mes] = 1
                    
    # Convertir a lista de tuplas y ordenar alfabéticamente (lo cual ordena los meses del 01 al 12)
    resultado = sorted(conteo_meses.items())
    
    return resultado
