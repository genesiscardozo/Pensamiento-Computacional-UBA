#Función para saludar
def saludar():
  print("Hola!")
  print("Espero que estés muy bien! :)")
  
saludar()

def saludo_venecia():
  print("Hola, Vene Bubu!")

def saludo_mimi():
  print("Hola, Mimi!")

saludo_venecia()
saludo_mimi()

#Función que recibe el nombre de una persona y la saluda
def nombrePersona(nombre):
  print("Hola " + nombre + " Espero que estés muy bien!")

nombrePersona("Andrés")
nombrePersona("Sasha")

#Practicaremos Parámetros
#Función que muestra la suma de 2 valores.

def mostrar_suma(sumando_1, sumando_2):
  suma = sumando_1 + sumando_2
  print("La suma es: ", suma)

mostrar_suma(3, 13)

#Función que muestra cosas y devuelve valores:
#Recibe 2 números y devuelve la suma de ellos.

def sumas(sumando_1, sumando_2):
  resultado = sumando_1 + sumando_2
  return resultado

resultado_suma = sumas(5, 9)
print(resultado_suma)

resultado_suma = sumas(30, 9)
print(resultado_suma)

#Recibe 2 números y devuelve la suma y la resta de ellos:
def resultados(numero_1, numero_2):
  suma = numero_1 + numero_2
  resta = numero_1 - numero_2
  return suma, resta
  
suma, resta = resultados(30, 18)
print("La suma es ", suma)
print("La resta es ", resta)
