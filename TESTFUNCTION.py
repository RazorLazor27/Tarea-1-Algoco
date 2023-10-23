# NO INCLUIR EN LA ENTREGA DEL PROYECTO FINAL
# Funcion llamada para hacer el proceso de testeo facil

import os


def data_input():


    # Define the directory path where the files are located
    current_directory = os.getcwd()
    print(current_directory)
    directory_path = f'{current_directory}/test_cases'

    # Create an empty list to store the tuples
    
    list_of_lists = []

    # Loop through all the files in the directory
    for filename in os.listdir(directory_path):

        if filename.startswith('input-') and filename.endswith('.dat'):
            # Open the file and read its contents
            with open(os.path.join(directory_path, filename), 'r') as file:
                # Read the first line of the file to get the number of trios
                

                while True:
                    linea = file.readline().strip()
                    if not linea:
                        break
                    else:
                        print(linea)

                    num_trios = int (linea)
                    
                    trios = []
                    for _ in range(num_trios):
                        trio = list(map(int, file.readline().strip().split()))
                        trios.append(trio)
                    
                    list_of_lists.append(trios)
    return list_of_lists



def data_output():
    current_directory = os.getcwd()
    print(current_directory)
    directory_path = f'{current_directory}/test_cases'

    list_of_list = []

    for filename in os.listdir(directory_path):
        if filename.startswith('output-') and filename.endswith('.dat'):
            # Open the file and read its contents
            with open(os.path.join(directory_path, filename), 'r') as file:
                # Create an empty list to store the numbers
                
                # Loop through each line in the file and append it to the list
                for line in file:
                    number = int(line.strip())
                    list_of_list.append(number)
    return list_of_list


