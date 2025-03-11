
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


