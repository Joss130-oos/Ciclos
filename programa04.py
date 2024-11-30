'''
Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
'''

for numero in range(1, 6):
    print(f"Tabla de multiplicar del { numero }:")
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{ numero } x { multiplicador } = { resultado }")
    print("-" * 25)