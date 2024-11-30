'''
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
y la media de todos los números introducidos.

Para este problema se requiere de un acumulador y un contador

Contador: Variable que va, como su nombre lo indica, contando elementos (interaciones),
por cada interación el contador va incrementando en 1

Ejemplo:
contador = 0
for i in range(5):
    contador = contador + 1
print(contador)

Acumulador: Variable que va, como su nombre lo indica, acumulando valores en cada interación,
por cada interación al valor inicial se le suman nuevos valores al acumulador

Ejemplo:
acumulador = 0;
for i in range(5):
    acumulador = acumulador + i
print(acumulador)
'''

print("Introduce algunos números (escribe 0 para terminar):")
acumulador = 0
contador = 0
while True:
    numero = int(input("Número: "))
    if numero == 0:
        break
    acumulador += numero
    contador += 1
if contador > 0:
    media = acumulador / contador
    print(f"Suma de los números: { acumulador }")
    print(f"Media de los números: { media }")
else:
    print("No se introdujeron números.")