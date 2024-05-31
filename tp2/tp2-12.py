"""
Un banco necesita para sus cajeros automáticos un programa que lea una cantidad de dinero e imprima a cuántos billetes equivale, considerando que existen billetes de 
$1000, $500, $100, $50, $10, $5 y $1. Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero.
"""
#COMPLETAR ESTE EJERCICIO, FIJARME SI ESTÁ BIEN

#Variables iniciales:
cantidadDinero = int(input("Ingrese la cantidad de dinero que desea extraer: "))

billete1000 = 1000
billete500 = 500
billete100 = 100
billete50 = 50
billete10 = 10
billete5 = 5
billete1 = 1

billetesTotales1000 = cantidadDinero / billete1000
billetesTotales500 = cantidadDinero / billete500
billetesTotales100 = cantidadDinero / billete100
billetesTotales50 = cantidadDinero / billete50
billetesTotales10 = cantidadDinero / billete10
billetesTotales5 = cantidadDinero / billete5
billetesTotales1 = cantidadDinero / billete1

minimaBilletes1000 = cantidadDinero / billete1000
minimaBilletes500 = cantidadDinero / billete500s
minimaBilletes100 = cantidadDinero / billete100
minimaBilletes50 = cantidadDinero / billete50
minimaBilletes10 = cantidadDinero / billete10

#Imprimimos el monto ingresado y el equivalente en billetes:
print("El monto que desea extraer es de", cantidadDinero)
print(cantidadDinero, "pesos, lo que equivale a:")
print(minimaBilletes1000, "billetes de 1000")
print(minimaBilletes500, "billetes de 500")
print(minimaBilletes100, "billetes de 100")
print(minimaBilletes50, "billetes de 50")
print(minimaBilletes10, "billetes de 10")

#Imprimimos la cantidad mínima de billetes que se pueden entregar:

print("La menor cantidad de billetes que se puede entregar para el monto es de: ")
print(billete1000, billete500, billete100, billete50, billete10, billete5, billete1, "billetes")

