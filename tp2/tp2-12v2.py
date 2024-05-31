# Programa para cajero automático en Python

# Definición de billetes
billete_1000 = 1000
billete_500 = 500
billete_100 = 100
billete_50 = 50
billete_10 = 10
billete_5 = 5
billete_1 = 1

# Ingreso de monto a retirar
cantidad_dinero = int(input("Ingrese la cantidad de dinero que desea extraer: "))

# Cálculo de la cantidad mínima de billetes
billetes_1000 = cantidad_dinero // billete_1000
resto_1000 = cantidad_dinero % billete_1000

billetes_500 = resto_1000 // billete_500
resto_500 = resto_1000 % billete_500

billetes_100 = resto_500 // billete_100
resto_100 = resto_500 % billete_100

billetes_50 = resto_100 // billete_50
resto_50 = resto_100 % billete_50

billetes_10 = resto_50 // billete_10
resto_10 = resto_50 % billete_10

billetes_5 = resto_10 // billete_5
resto_1 = resto_10 % billete_5

billetes_1 = resto_1 // billete_1

# Impresión del resultado
print(f"El monto que desea extraer es de ${cantidad_dinero}")
print(f"Equivalente a:")
print(f"{billetes_1000} billetes de $1000") if billetes_1000 > 0 else ""
print(f"{billetes_500} billetes de $500") if billetes_500 > 0 else ""
print(f"{billetes_100} billetes de $100") if billetes_100 > 0 else ""
print(f"{billetes_50} billetes de $50") if billetes_50 > 0 else ""
print(f"{billetes_10} billetes de $10") if billetes_10 > 0 else ""
print(f"{billetes_5} billetes de $5") if billetes_5 > 0 else ""
print(f"{billetes_1} billetes de $1") if billetes_1 > 0 else ""

print(f"\nLa menor cantidad de billetes que se puede entregar es de:")
print(f"{billetes_1000 + billetes_500 + billetes_100 + billetes_50 + billetes_10 + billetes_5 + billetes_1} billetes")