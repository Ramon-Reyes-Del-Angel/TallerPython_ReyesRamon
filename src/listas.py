# listas.py

def ejemplos_listas():
    # Promedio de calificaciones
    calif = [4, 6, 9, 7, 5]

    # Forma 1
    suma = 0
    for i in range(len(calif)):
        suma += calif[i]
    prom = suma / len(calif)
    print(prom)

    # Forma 2
    op = 0
    for e in calif:
        op += e
    print(f'Promedio: {op / len(calif)}')

    # Captura de datos del usuario en lista
    cantidad = int(input('Cantidad de datos: '))
    lista = []
    for i in range(cantidad):
        lista.append(int(input('Value: ')))
    print(lista)

    # Actividad 2: Contar pares y corregir impares
    lista = []
    listaCorregida = []
    cont = 0
    for i in range(15):
        num = int(input("Value: "))
        lista.append(num)
        if num % 2 != 0:
            listaCorregida.append(num + 1)
        else:
            listaCorregida.append(num)
            cont += 1

    print("Lista:", lista)
    print(f"Cantidad de números pares: {cont}")
    print("Lista corregida:", listaCorregida)
