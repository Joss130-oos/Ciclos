'''
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
'''

cant_num = int(input("¿Cuántos números quieres introducir? "))
mayores_cero = 0
menores_cero = 0
iguales_cero = 0
for i in range(cant_num):
    numero = float(input(f"Número {i + 1}: "))
    if numero > 0:
        mayores_cero += 1
    elif numero < 0:
        menores_cero += 1
    else:
        iguales_cero += 1
print(f"Números mayores que 0: {mayores_cero}")
print(f"Números menores que 0: {menores_cero}")
print(f"Números iguales a 0: {iguales_cero}")