#Calcular el promedio de las notas que obtiene un alumno al rendir los dos parciales.
parcial1 = int(input("Ingrese su nota del primer parcial "))
parcial2 = int(input("Ingrese su nota del segundo parcial "))

sumaParciales = parcial1 + parcial2
promedio = sumaParciales / 2

print("Su promedio es " + str(promedio))