# main.py
# Archivo principal del proyecto

import impresiones
import operaciones
import ciclos
import listas
import archivos

def main():
    print("-> MENÚ PRINCIPAL <-")
    print("1. Impresiones")
    print("2. Operaciones")
    print("3. Ciclos")
    print("4. Listas")
    print("5. Archivos")
    print("0. Salir")

    opc = int(input("Elige una opción: "))

    if opc == 1:
        impresiones.ejemplos_impresiones()

    elif opc == 2:
        operaciones.ejemplos_operaciones()

    elif opc == 3:
        ciclos.ejemplos_ciclos()

    elif opc == 4:
        listas.ejemplos_listas()

    elif opc == 5:
        archivos.ejemplos_archivos()

    elif opc == 0:
        print("Saliendo...")

    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()
