'''
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''

def es_primo(num):
    """Función que determina si un número es primo."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def mostrar_primos(cantidad):
    """Función que muestra los primeros 'cantidad' números primos."""
    primos_encontrados = 0
    num = 2
    while primos_encontrados < cantidad:
        if es_primo(num):
            print(num)
            primos_encontrados += 1
        num += 1
cantidad = int(input("¿Cuántos números primos quieres mostrar? "))
mostrar_primos(cantidad)