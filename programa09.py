'''
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
'''

while True:
    try:
        limite_inferior = int(input("Introduce el límite inferior de un intervalo: "))
        limite_superior = int(input("Introduce el límite superior de un intervalo: "))
        if limite_inferior < limite_superior:
            break
        print("El límite inferior debe ser menor, al límite superior. Intenta otra vez.")
    except ValueError:
        print("Por favor, introduce un valor númerico válido.")
suma_dentro = 0
fuera_intervalo = 0
igual_limites = False
print("Introduce números (0 para terminar):")
while True:
    try:
        numero = int(input())
        if numero == 0:
            break
        if limite_inferior < numero < limite_superior:
            suma_dentro += numero
        elif numero != limite_inferior and numero != limite_superior:
            fuera_intervalo += 1
        if numero == limite_inferior or numero == limite_superior:
            igual_limites = True
    except ValueError:
            print("Introduce un número válido.")
print("Resultados:")
print(f"Suma de los números dentro del intervalo ({ limite_inferior }, { limite_superior }): { suma_dentro }")
print(f"Números fuera del intervalo: { fuera_intervalo }")
print("Se ha introducido un número igual alos límites del intervalo: " + ("Sí" if igual_limites else "No"))