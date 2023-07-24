import random

'''
Función encargada de crear la matriz.
Devuelve una matriz N x N con números aleatorios
'''
def generarMatriz(): 
    print("El tamaño de la matriz es", n)
    for i in range(n):
        fila = []
        for j in range(n):
            # Se rellena la fila i 
            fila.append(random.randint(0,9))
        # Se añade la fila completa a la matriz
        matriz.append(fila)
        
    #Se imprime matriz por filas
    for fila in matriz:
        print(fila)
        
    return matriz
            

# Suma los elementos de la fila f de la matriz     
def sumarFila(matriz, f):
    sumaF = 0
    for i in range(n):
        sumaF += matriz[f][i]
    return sumaF

# Suma los elementos de la columna c de la matriz
def sumarColumna(matriz, c):
    sumaC = 0
    for j in range(n):
        sumaC += matriz[j][c]
    return sumaC
    

# Excepcion creada para controlar que el valor introducido sea un número positivo
class valueNegativ(Exception):     
    print("El valor introducido debe ser un número positivo")


if __name__ == '__main__':
    try:
        n = int(input("Ingrese el tamaño de la matriz (N): \n"))
        if(n <= 0):
            raise valueNegativ
        # Creamos la matriz vacia
        matriz = []

        matriz = generarMatriz()

        # Creamos las listas que contendrán las sumas de los elementos de las filas y las columnas respectivamente
        sumaFilas = []
        sumaColumnas = []

        # Bucle que rellena las listas con los resultadas obtenidos al sumar los elementos por filas y por columnas
        for x in range(n):
            sumaFilas.append(sumarFila(matriz,x))
            sumaColumnas.append(sumarColumna(matriz,x))
            
        print("Suma de filas", sumaFilas)
        print("Suma de columnas: ", sumaColumnas)
    except ValueError:
        # Captura error si el valor de n no es un digito
        print("El valor introducido debe ser un dígito")
    