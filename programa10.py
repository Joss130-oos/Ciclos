'''
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
'''

def calcular_potencia(base, exponente):
  if exponente < 0:
    return "El exponente debe ser un número entero positivo."
  resultado = 1
  for _ in range(exponente):
    resultado *= base
  return resultado
try:
  base = float(input("Introduce la base (debe ser un número real): "))
  exponente = int(input("Introduce un exponente (debe ser un número entero positivo): "))
  print(f"El resultado de { base } elevado a la potencia { exponente } es: {calcular_potencia(base, exponente)}")
except ValueError:
  print("Error, debes introducir valores válidos.")