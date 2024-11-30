'''
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
'''

print("Introduce 10 números para poder calcular su promedio:")
acumulador = 0
contador = 0
for i in range(10):
    numero = float(input(f"Número {i + 1}: "))
    acumulador += numero
    contador += 1
promedio = acumulador / contador
print(f"La suma de estos números es: {acumulador}")
print(f"Y por lo tanto su promedio es: {promedio}")