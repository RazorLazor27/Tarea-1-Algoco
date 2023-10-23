import flujo_datos as test

def initial_input(cajas):
    rotaciones = []
    for caja in cajas:
        rotaciones.append([max(caja[0], caja[1]), min(caja[0], caja[1]), caja[2]])
        rotaciones.append([max(caja[0], caja[2]), min(caja[0], caja[2]), caja[1]])
        rotaciones.append([max(caja[1], caja[2]), min(caja[1], caja[2]), caja[0]])

    rotaciones.sort(key=lambda x: x[0]*x[1], reverse=True)

    return rotaciones

def Pregunta_1(cajas, indice=-1):
    max_tamano = 0
    for i in range(len(cajas)):
        if indice == -1 or cajas[i][0] < cajas[indice][0] and cajas[i][1] < cajas[indice][1]:
            tamano = Pregunta_1(cajas, i)
            max_tamano = max(max_tamano, tamano)

    if (indice != -1):
        max_tamano += cajas[indice][2]
    else: 
        max_tamano += 0
    # max_tamano += cajas[indice][2] if indice != -1 else 0
    return max_tamano

def Pregunta_2(cajas, indice=-1):
    memoization = {}
    def aux(cajas, indice):
        if indice in memoization:
            return memoization[indice]
        max_tamano = 0
        for i in range(len(cajas)):
            if indice == -1 or cajas[i][0] < cajas[indice][0] and cajas[i][1] < cajas[indice][1]:
                tamano = aux(cajas, i)
                max_tamano = max(max_tamano, tamano)
        max_tamano += cajas[indice][2] if indice != -1 else 0
        memoization[indice] = max_tamano
        return max_tamano
    return aux(cajas, indice)

Entradas = test.data_input()
Salidas = test.data_output()

for i in range(len(Salidas)):
    num1 = Pregunta_1(initial_input(Entradas[i]))
    num2 = Pregunta_2(initial_input(Entradas[i]))

    print(f"La entrada fue: {Entradas[i]} \ndonde la primera funcion entrega: {num1} y la segunda funcion retorna: {num2} y el resultado esperado es: {Salidas[i]}\n")
input("Ingrese una tecla para salir de esto")
