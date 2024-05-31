"""
Una inmobiliaria paga a sus vendedores un salario de $250000, más una comisión de $50000 por cada venta realizada, más el 5% del valor de las ventas. 
Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes. 
Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.
"""

#Ingresamos las variables iniciales:
salario = 250000
comision = 50000
porcentaje = 0.5

#Solicitamos el número de vendedor, las cantidad de ventas y el valor total de ventas por pantalla:
numeroVendedor = int(input("Ingrese su Número de Vendedor: "))
cantidadVentas = int(input("Ingrese la cantidad de ventas realizadas: "))
valorTotal = int(input("Ingrese el valor de las ventas: "))

#Calculamos porcentajes y Comisiones:
porcentajeAdicional = valorTotal * porcentaje
comisionesVentas = cantidadVentas * comision

salarioTotal = salario + porcentajeAdicional + comisionesVentas

#Imprimimos el número de vendedor y el salario que le corresponde determinado mes:
print("Su número de vendedor es:", numeroVendedor)
print("La cantidad de ventas que realizó es de:", cantidadVentas)
print("El valor total de las ventas es de:", salarioTotal)

