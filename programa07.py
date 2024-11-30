'''
Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''

while True:
    caracter = input("Introduce un carácter y da espacio para terminar: ").lower()
    if caracter == " ":
        print("Programa terminado.")
        break
    elif caracter in "aeiou":
        print("VOCAL")
    else:
        print("NO VOCAL")