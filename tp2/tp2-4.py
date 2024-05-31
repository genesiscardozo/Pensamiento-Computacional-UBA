#Escribir un programa que permita ingresar la edad de una persona en años y la
#convierta a días, imprimiendo el resultado. Considerar que todos los años tienen 365 días.

#PROGRAMA PARA INGRESAR LA EDAD DE UNA PERSONA EN AÑOS, CONVERTIR A DÍAS E IMPRIMIR RESULTADO:
edad = int(input("Ingresa tu edad "))
edadEnDias = edad * 365

print("Su edad en días es " + str(edadEnDias))