'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
'''

primer_pago = 10
razon = 2
meses = 20
pagos_mens = [primer_pago * (razon ** (mes - 1)) for mes in range(1, meses + 1)]
total = sum(pagos_mens)
print("Pagos mensuales: ")
for mes, pago in enumerate(pagos_mens, start=1):
    print(f"Mes { mes }: { pago } euros")
print(f"Total pagado después de { meses } meses: { total } euros")