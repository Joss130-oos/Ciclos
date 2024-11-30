'''
Escribir un programa que imprima todos los números pares entre dos números que 
se le pidan al usuario.
'''

inicio = int(input("Introduce un primer número: "))
fin = int(input("Introduce segundo número: "))
if inicio > fin:
    inicio, fin = fin, inicio
print(f"Números pares entre {inicio} y {fin}:")
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        print(numero)