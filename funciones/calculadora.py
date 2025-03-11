## calculadora.py

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




