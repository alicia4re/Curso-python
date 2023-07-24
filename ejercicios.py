'''
EJERCICIO 1: 
1. Dados dos números, escriba un código Python para encontrar el mínimo de estos dos números
'''
def calcularMin(a,b):
    return min(a,b)
calcularMin(76,4)


'''
EJERCICIO 2
Invertir palabras de una cadena dada.
'''
def invertir(s):
    palabra = s.split()
    reverse = ' '.join(reversed(palabra))
    return reverse
invertir('Hola, esto es una prueba')

'''
EJERCICIO 3
3. Realizar una suma de los elementos de una tupla
'''

