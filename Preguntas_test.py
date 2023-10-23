import Tarea1
import TESTFUNCTION as test
import pytest
# intento fallido por que solo funciona para pregunta 1

entradas = test.data_input()

salidas = test.data_output()


@pytest.mark.parametrize(
        ('input_n', 'expected'),
        (
            
            (entradas[0],salidas[0]),
            (entradas[1],salidas[1]),
            (entradas[2],salidas[2]), 
            (entradas[3],salidas[3]), 
            (entradas[4],salidas[4]), 
            (entradas[5],salidas[5]),
            (entradas[6],salidas[6]), 
            (entradas[7],salidas[7]), 
            (entradas[8],salidas[8]), 
            (entradas[9],salidas[9]), 
            (entradas[10],salidas[10]), 
            (entradas[11],salidas[11]),     
            (entradas[12],salidas[12]), 
            (entradas[13],salidas[13]), 
            (entradas[14],salidas[14]), 
            (entradas[15],salidas[15]), 
            (entradas[16],salidas[16]),  

        )
)


def test_Pregunta1(input_n, expected):
    assert Tarea1.Pregunta_1(Tarea1.initial_input(input_n)) == expected

def test_Pregunta2(input_n, expected, memo={}):
    assert Tarea1.Pregunta_2(Tarea1.initial_input(input_n)) == expected

    

