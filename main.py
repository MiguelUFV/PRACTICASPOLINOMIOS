from funciones.calculadora import parse_polinomio, suma, resta, multiplica, divide, imprime_polinomio, evalua
from funciones.leer_fichero import leer_desde_fichero

def main():
    while True:
        print("\nCalculadora de Polinomios")
        print("1) Ingresar datos manualmente")
        print("2) Leer desde fichero")
        print("3) Salir")
        opcion_ingreso = input("Elige una opción: ")

        if opcion_ingreso == '3':
            break

        if opcion_ingreso == '2':
            nombre_fichero = input("Introduce el nombre del fichero: ")
            operacion, polinomios = leer_desde_fichero(nombre_fichero)
            if operacion is None:
                continue  # Volver al inicio si hubo un error
        else:
            print("\nOperaciones disponibles:")
            print("1) Sumar")
            print("2) Restar")
            print("3) Multiplicar")
            print("4) Dividir")
            print("5) Evaluar")
            print("6) Salir")
            opcion = input("Elige una opción: ")

            if opcion == '6':
                break

            if opcion == '5':
                p = parse_polinomio(input("Escribe el polinomio a evaluar (ej: 3x^2+3x+1): "))
                x = float(input("Introduce el valor de x: "))
                print("Resultado de la evaluación:", evalua(p, x))
                continue

            p1 = parse_polinomio(input("Escribe el primer polinomio (ej: 3x^2+3x+1): "))
            p2 = parse_polinomio(input("Escribe el segundo polinomio (ej: x^2-1): "))

        # Determinar la operación y los polinomios si vienen de un fichero
        if opcion_ingreso == '2':
            p1 = parse_polinomio(polinomios[0])
            p2 = parse_polinomio(polinomios[1]) if len(polinomios) > 1 else None
            opcion = {'suma': '1', 'resta': '2', 'multiplica': '3', 'divide': '4', 'evalua': '5'}.get(operacion)

        if opcion == '1':
            resultado = suma(p1, p2)
            print("Resultado:", imprime_polinomio(resultado))
        elif opcion == '2':
            resultado = resta(p1, p2)
            print("Resultado:", imprime_polinomio(resultado))
        elif opcion == '3':
            resultado = multiplica(p1, p2)
            print("Resultado:", imprime_polinomio(resultado))
        elif opcion == '4':
            cociente, residuo = divide(p1, p2)
            print("Cociente:", imprime_polinomio(cociente) if cociente else "0")
            print("Residuo:", imprime_polinomio(residuo) if residuo else "0")
        elif opcion == '5':
            x = float(polinomios[1]) if len(polinomios) > 1 else float(input("Introduce el valor de x: "))
            print("Resultado de la evaluación:", evalua(p1, x))
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()

