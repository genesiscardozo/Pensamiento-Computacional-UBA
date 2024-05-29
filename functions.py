#This code was created on: August 23, 2023

def naming(name):
  print("Hello " + name + " I hope you're doing well!") 

#"Say Hello" Function
def greetings():
  print("Hello!")
  print("How's it going?")
  
greetings()

def hello_venecia():
  print("Hello, Vene Bubu!")

def hello_mimi():
  print("Hello, Mimi!")

hello_venecia()
hello_mimi()

#Function that receives someone's name and says hello
def someonesName(name):
  print("Hey " + name + " I hope you had a lovely wekeend!")

someonesName("Andrew")
someonesName("Sasha")

#Practice parameters
#Function that shows the sum of two values:

def show_addition(addingup_1, addingup_2):
  addition = addingup_1 + addingup_2
  print("The result of the sum is: ", addition)

show_addition(3, 13)

#Function that shows things and returns values: 
#Receives 2 numbers and returns their sum
 
def sums(addingup_1, addingup_2):
  result = addingup_1 + addingup_2
  return result

result_sum = sums(5, 9)
print(result_sum)

result_sum = sums(30, 9)
print(result_sum)

#Receives 2 numbers and returns the sum and the subtraction of them.
def results(number1, number2):
  addition = number1 + number2
  subtraction = number1 - number2
  return addition, subtraction
  
addition, subtraction = results(30, 18)
print("The result of the sum is ", addition)
print("The result of the subtraction is ", subtraction)
