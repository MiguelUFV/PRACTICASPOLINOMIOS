from funciones.calculadora import parse_polinomio, suma, resta, multiplica, imprime_polinomio


def main():
    while True:
        print("\nCalculadora de Polinomios")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Salir")
        opcion = input("Elige una opción: ")

        if opcion == '4':
            break

        p1 = parse_polinomio(input("Escribe el primer polinomio (ej: 3x^2+3x+1): "))
        p2 = parse_polinomio(input("Escribe el segundo polinomio (ej: x^2-1): "))

        if opcion == '1':
            resultado = suma(p1, p2)
        elif opcion == '2':
            resultado = resta(p1, p2)
        elif opcion == '3':
            resultado = multiplica(p1, p2)
        else:
            print("Opción no válida")
            continue

        print("Resultado:", imprime_polinomio(resultado))

if __name__ == "__main__":
    main()

