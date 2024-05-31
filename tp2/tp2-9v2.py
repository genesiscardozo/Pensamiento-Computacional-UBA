"""
Una inmobiliaria paga a sus vendedores un salario de $250000, más una comisión de $50000 por cada venta realizada, más el 5% del valor de las ventas. 
Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes. 
Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.


Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes. 
Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.
"""

#Variables Iniciales
SALARIO_BASE = 250000
COMISION_POR_VENTA = 50000
PORCENTAJE_ADICIONAL = 0.05

# Acumulador de salario total
acumulador_salario_total = 0

# Bucle para procesar cada vendedor
while True:
    # Leer el número de vendedor
    numero_vendedor = int(input("Ingrese el número de vendedor (o 0 para finalizar): "))

    # Si el número de vendedor es 0, finalizar el bucle
    if numero_vendedor == 0:
        break

    # Leer la cantidad de ventas realizadas
    cantidad_ventas = int(input("Ingrese la cantidad de ventas realizadas: "))

    # Leer el valor total de las ventas
    valor_total_ventas = float(input("Ingrese el valor total de las ventas: $ "))

    # Calcular la comisión por ventas
    comision_ventas = cantidad_ventas * COMISION_POR_VENTA

    # Calcular el porcentaje adicional
    porcentaje_adicional = valor_total_ventas * PORCENTAJE_ADICIONAL

    # Calcular el salario total
    salario_total = SALARIO_BASE + comision_ventas + porcentaje_adicional

    # Acumular el salario total
    acumulador_salario_total = acumulador_salario_total + salario_total

    # Imprimir el número de vendedor y el salario total
    print("Número de vendedor:", numero_vendedor)
    print("Salario total:", salario_total)

# Imprimir el salario total acumulado
print("\nSalario total acumulado:", acumulador_salario_total)