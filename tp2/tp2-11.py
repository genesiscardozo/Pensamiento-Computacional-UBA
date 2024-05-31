"""
Leer un período en segundos e imprimirlo expresado en días, horas, minutos y segundos. 
Por ejemplo, 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos. 
"""

#Pedimos una entrada para ingresar cuánto tiempo toma hacer una tarea en segundos: 
segundos = int(input("Ingrese cuántos segundos tomó hacer la tarea: "))

#Agregamos las variables para día, hora, minuto y segundos. 
dias = segundos // (24 * 3600)
horas = segundos // 3600
minutos = segundos // 60

print(segundos, "segundos, equivalen a:", dias, "días", horas, "horas", minutos, "minutos")
