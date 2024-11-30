'''
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
'''

try:
  total = 0
  ahorros_mens = []
  for mes in range(1, 13):
      deposito = float(input(f"Ingresa el dinero ahorrado al final del mes {mes}: "))
      total += deposito
      ahorros_mens.append(total)
      print(f"Total ahorrado en el mes {mes}: {total:.2f} pesos\n")
  print(f"\nTotal ahorrado al final del año: {total:.2f} pesos")
except ValueError:
   print("Error, ingresa números para determinar los ahorros.")