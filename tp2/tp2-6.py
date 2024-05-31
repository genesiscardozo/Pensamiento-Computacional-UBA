"""
Tres personas aportan dinero para fundar una empresa 
(no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una.
"""
#Ingresamos los nombres de las tres personas que aportan dinero
nombre1 = input("Hola, ingrese su nombre: ")
nombre2 = input("Hola, ingrese su nombre: ")
nombre3 = input("Hola, ingrese su nombre: ")

#Variables para la inversión inicial de cada persona
persona1 = int(input("Hola, " + nombre1 + " ingrese el dinero que va a invertir en la empresa: "))
persona2 = int(input("Hola, " + nombre2 + " ingrese el dinero que va a invertir en la empresa: "))
persona3 = int(input("Hola, " + nombre3 + " ingrese el dinero que va a invertir en la empresa: "))

#Variable para calcular el total de la inversión
totalInversión = persona1 + persona2 + persona3

#Porcentaje de Inversión de cada persona
porcentaje_persona1 = (persona1 / totalInversión) * 100
porcentaje_persona2 = (persona2 / totalInversión) * 100
porcentaje_persona3 = (persona3 / totalInversión) * 100

#Mostramos los resultados por pantalla:
print("El total de la inversión de " + nombre1 + " es de: ", str(porcentaje_persona1))
print("El total de la inversión de " + nombre2 + " es de: ", str(porcentaje_persona2))
print("El total de la inversión de " + nombre3 + " es de: ", str(porcentaje_persona3))