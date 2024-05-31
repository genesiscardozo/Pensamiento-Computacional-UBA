"""
Un productor agrícola desea estimar cuántos quintales de trigo puede producir en su parcela. 
Escribir un programa para ingresar el largo y el ancho en metros de la misma y determinar el rinde sabiendo que en 10m2 se obtienen 2 quintales.

#Determinar cuánto rinde la parcela si en 10m2 se obtienen 2 quintales
"""
#Variables iniciales:
largo = float(input("Ingrese el largo de la parcela en metros: "))
ancho = float(input("Ingrese el ancho de la parcela en metros: "))

#Calculamos el área de la parcela:
tamanoParcela = largo * ancho

#Rendimiento por metro cuadrado:
rindeParcela = 2 / 10 

#Rendimiento total: 
rendimiento = rindeParcela * tamanoParcela

print("El tamaño de la parcela es de", largo, "metros de largo, por", ancho, "metros de ancho. Es decir", tamanoParcela, "metros cuadrados.")
print("La parcela tiene un rinde de", rendimiento, "quintales de trigo")
