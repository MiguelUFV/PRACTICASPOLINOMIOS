def parse_polinomio(polinomio_str):
    terminos = polinomio_str.replace('-', '+-').split('+')
    polinomio = {}
    for termino in terminos:
        termino = termino.strip()
        if 'x^' in termino:
            coef, exp = termino.split('x^')
            exp = int(exp)
        elif 'x' in termino:
            coef = termino.replace('x', '')
            exp = 1
        else:
            coef = termino
            exp = 0
        coef = float(coef) if coef else 1.0
        polinomio[exp] = polinomio.get(exp, 0) + coef
    return polinomio

def suma(p1, p2):
    resultado = p1.copy()
    for exp, coef in p2.items():
        resultado[exp] = resultado.get(exp, 0) + coef
    return resultado

def resta(p1, p2):
    resultado = p1.copy()
    for exp, coef in p2.items():
        resultado[exp] = resultado.get(exp, 0) - coef
    return resultado

def multiplica(p1, p2):
    resultado = {}
    for exp1, coef1 in p1.items():
        for exp2, coef2 in p2.items():
            exp = exp1 + exp2
            coef = coef1 * coef2
            resultado[exp] = resultado.get(exp, 0) + coef
    return resultado


def divide(p1, p2):
    if not p2 or all(coef == 0 for coef in p2.values()):
        raise ValueError("No se puede dividir por un polinomio nulo o cero.")

    if max(p1.keys()) < max(p2.keys()):
        # Si el grado de p1 es menor que p2, la división no se puede realizar
        return {}, p1

    cociente = {}
    residuo = p1.copy()

    while residuo and max(residuo.keys()) >= max(p2.keys()):
        exp_dif = max(residuo.keys()) - max(p2.keys())
        coef_dif = residuo[max(residuo.keys())] / p2[max(p2.keys())]
        cociente[exp_dif] = coef_dif

        # Multiplicamos el divisor por el término del cociente calculado
        p2_aux = {exp + exp_dif: coef * coef_dif for exp, coef in p2.items()}

        # Restamos para actualizar el residuo
        residuo = resta(residuo, p2_aux)

        # Eliminamos términos con coeficiente cero
        residuo = {exp: coef for exp, coef in residuo.items() if coef != 0}

    return cociente, residuo


def imprime_polinomio(polinomio):
    terminos = []
    for exp in sorted(polinomio.keys(), reverse=True):
        coef = polinomio[exp]
        if coef:
            if exp == 0:
                terminos.append(f"{coef}")
            elif exp == 1:
                terminos.append(f"{coef}x")
            else:
                terminos.append(f"{coef}x^{exp}")
    return ' + '.join(terminos).replace('+ -', '- ')

def evalua(polinomio, x):
    resultado = 0
    for exp, coef in polinomio.items():
        resultado += coef * (x ** exp)
    return resultado
