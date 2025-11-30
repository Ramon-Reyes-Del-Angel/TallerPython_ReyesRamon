# impresiones.py

def ejemplos_impresiones():
    # Impresión básica en pantalla
    print('Hola mundo')
    print("Hola mundo")

    # Uso de múltiples argumentos en print()
    print('Hola', '', 'mundo')

    # Actividad 1: Imprimir nombre, apellidos y carrera
    nombre = 'Ramón'
    apellidos = 'Reyes Del Angel'
    carrera = 'ISC'
    print(f"{nombre} {apellidos} es de la carrera de {carrera}")
    print(f'{nombre} {apellidos} es de la carrera de {carrera}')

    # Uso de variables y diferentes formas de concatenar texto
    nombre = 'Jose'
    edad = 30
    carrera = 'Ciencia de Datos'
    semestre = '2do'
    print('Hola', nombre, 'de', carrera, 'es un viejo de', edad, 'años, y va en', semestre, 'semestre')
    print(f'Hola {nombre} de {carrera} es un viejo de {edad} años y va en {semestre} semestre')
    print('Hola ' + nombre + ' de la carrera de ' + carrera)

    # Captura de datos con input()
    nombre = input('¿Cómo te llamas? ')
    edad = input('Tu edad: ')
    estatura = float(input('Tu estatura: '))
    print(f'Hola {nombre} de {edad} años y mides: {estatura} m')
