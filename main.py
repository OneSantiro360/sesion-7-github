# Calculadora básica — práctica sesión 7

def sumar(a, b):
    '''Retorna la suma de dos números'''
    return a + b

def restar(a, b):
    '''Retorna la resta de dos números'''
    return a - b

def multiplicar(a, b):
    '''Retorna el producto de dos números'''
    return a * b

def dividir(a, b):
    '''Retorna la división de dos números'''
    if b == 0:
        raise ValueError('No se puede dividir entre cero')
    return a / b

if __name__ == '__main__':
    print(f'Suma: {sumar(10, 5)}')
    print(f'Resta: {restar(10, 5)}')
    print(f'Multiplicación: {multiplicar(10, 5)}')
    print(f'División: {dividir(10, 5)}')
