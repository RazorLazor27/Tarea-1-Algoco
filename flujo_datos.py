import os

def data_input():

    directorio_actual = os.getcwd()
    
    directorio_datos = f'{directorio_actual}/test_cases'

    
    lista_input = []

    # Busca todos los nombres en el directorio
    for nombre_archivo in os.listdir(directorio_datos):

        if nombre_archivo.startswith('input-') and nombre_archivo.endswith('.dat'):
    
            with open(os.path.join(directorio_datos, nombre_archivo), 'r') as archivo:
                
                while True:
                    linea = archivo.readline().strip()
                    if not linea:
                        break
                        

                    num_trios = int (linea)
                    
                    trios = []
                    for _ in range(num_trios):
                        trio = list(map(int, archivo.readline().strip().split()))
                        trios.append(trio)
                    
                    lista_input.append(trios)
    return lista_input


def data_output():
    directorio_actual = os.getcwd()
    #print(directorio_actual)
    directorio_datos = f'{directorio_actual}/test_cases'

    lista_output = []

    for nombre_archivo in os.listdir(directorio_datos):
        if nombre_archivo.startswith('output-') and nombre_archivo.endswith('.dat'):
            # Open the archivo and read its contents
            with open(os.path.join(directorio_datos, nombre_archivo), 'r') as archivo:
                
                for line in archivo:
                    number = int(line.strip())
                    lista_output.append(number)
                    
    return lista_output