def leer_desde_fichero(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) < 2:
                raise ValueError("El fichero debe contener al menos una operación y un polinomio.")

            operacion = lineas[0].strip()
            polinomios = [linea.strip() for linea in lineas[1:] if linea.strip()]

            if operacion not in ['suma', 'resta', 'multiplica', 'divide', 'evalua']:
                raise ValueError(f"Operación no válida en el fichero: {operacion}")

            return operacion, polinomios

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
        return None, None
    except ValueError as e:
        print(f"Error en el formato del archivo: {e}")
        return None, None
