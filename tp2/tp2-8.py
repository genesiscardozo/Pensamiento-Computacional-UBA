"""
Leer una medida en metros e imprimir esta medida expresada en centímetros, pulgadas, pies y yardas.
Los factores de conversión son:
· 1 pie = 12 pulgadas
· 1 yarda = 3 pies
· 1 pulgada = 2,54 cm.
· 1 metro = 100 cm.

Ordenamos las medidas:
1 metro = 100 cm
1 pulgada = 2.54 cm
1 pie = 12 pulgadas
1 yarda = 3 pies
"""

# Pedido de cantidad de metros
metros = float(input("Ingrese su medida en metros: "))

centimetro = metros * 100
pulgadas = centimetro / 2.54
pies = pulgadas / 12
yardas = pies / 3

#Imprimimos la cantidad de metros ingresados por teclado y lo convertimos a cm, pulgadas, pies y yardas
print("Su medida:" , str(metros) + " metros" + " en centímetros es " + str(centimetro) + ", en pulgadas es " + str(pulgadas) + " , en pies es " + str(pies) + ", en yardas es " + str(yardas))