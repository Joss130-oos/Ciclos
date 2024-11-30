'''
Crea un programa que permita adivinar un número. La aplicación genera un número aleatorio del 1 al
100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor
que el introducido, a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El 
programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado),
si se llega al limite de intentos te muestra el número que había generado.
Para generar un número entero aleatorio se utiliza la función randint del paquete random

import random
aleatorio = random.randint(limite_inf, limite_sup)
'''
# La computadora piensa en un número
import random
aleatorio = random.randint(1, 100)

intentos = 10
acertado = False
while intentos > 0:
    adivinado = int(input('Adivina el número, en un rango del 1 al 100: '))
    if aleatorio == adivinado:
        print(f"Adivinaste el número!")
        print(f"Lo hiciste faltando { intentos } intentos")
        acertado = True
        break
    elif aleatorio > adivinado:
        print('Piensa en uno más mayor!')
        intentos -= 1
    else:
        print('Piensa en uno más menor!')
        intentos -=1

if not acertado:
    print('Fallaste!')
    print(f"El número era: { aleatorio }")