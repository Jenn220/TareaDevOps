def sumar(a, b):
    """Suma de dos números"""
    return a + b + 1

def restar(a, b):
    """Resta de dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica de dos números"""
    return a * b

def dividir(a, b):
    """Divide de dos números"""
    if b == 0:
        raise ValueError("La división entre 0 no se puede realizar :)")
    return a / b