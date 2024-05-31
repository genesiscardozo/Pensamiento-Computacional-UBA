""""
Calcular el descuento y el importe a pagar por un medicamento adquirido en una farmacia. 
El precio del mismo se ingresa por teclado. La farmacia realiza un descuento del 35% 
a todos los medicamentos. Se solicita mostrar el precio original, el monto del descuento 
y el importe final a pagar
"""

#Solicitamos ingresar el precio por teclado:
precio_medicamento = int(input("Ingrese el precio del medicamento: "))
#Calculamos el descuento del 35%
descuento = precio_medicamento * 0.35
#Calculamos el importe final restando el descuento
importe_final = precio_medicamento - descuento 

#Imprimimos el precio original, el descuento y el precio final
print("El precio original es ", str(precio_medicamento))
print("El monto del descuento es de: ", str(descuento))
print("El importe final a pagar es: ", str(importe_final))