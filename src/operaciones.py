# operaciones.py

def ejemplos_operaciones():
    # Variables numéricas
    x = 9
    y = 15

    # Operaciones aritméticas con f-strings
    print(f'La suma de los números es: {x + y}')
    print(f'La resta de los números es: {x - y}')
    print(f'La multiplicación de los números es: {x * y}')
    print(f'La división de los números es: {int(x / y)}')

    # Calculadora básica con menú
    x = int(input('Primer valor: '))
    y = int(input('Segundo valor: '))

    print('¿Qué operación desea?:')
    print(' 1) Suma')
    print(' 2) Resta')
    print(' 3) Multiplicación')
    print(' 4) División')

    operacion = int(input())

    if operacion == 1:
        print(f'La respuesta es: {x + y}')
    elif operacion == 2:
        print(f'La respuesta es: {x - y}')
    elif operacion == 3:
        print(f'La respuesta es: {x * y}')
    elif operacion == 4:
        print(f'La respuesta es: {x / y}')
