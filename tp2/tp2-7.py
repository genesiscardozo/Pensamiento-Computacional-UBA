"""
Una persona invierte su capital en un banco y desea saber cuánto dinero ganará en un mes, 
teniendo en cuenta que el banco paga 2% mensual. ¿Cuánto ganará en 6 meses si deja su dinero invertido?
"""
#Variable para ingresar la inversión inicial:
capitalInvertido = int(input("Ingrese el dinero que desea invertir: "))
gananciaBanco = 0.02

inversionPorMes = capitalInvertido * gananciaBanco
inversionSeisMeses = inversionPorMes * 6
gananciaTotal = inversionSeisMeses + capitalInvertido

#Imprimimos por pantalla los resultados:
print("Su inversión es de: " + str(capitalInvertido))
print("Su ganancia por mes es de: " + str(inversionPorMes))
print("Su ganancia en 6 meses será de: " + str(inversionSeisMeses))
print("En 6 meses, su ganancia, más su inversión inicial será de: " + str(gananciaTotal))