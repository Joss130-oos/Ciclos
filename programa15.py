'''
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
'''

try:
    numero = int(input("Introduce un número entero: "))
    binario = bin(numero)
    print(f"El número {numero} en binario es: {binario[2:]}")
except ValueError:
    print("Error, se debe ingresar un número entero")