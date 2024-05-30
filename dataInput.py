#DATA INPUT EXERCISES:

#FIRST EXCERCISE:
#Create a program that asks the user for an integer and determines if it is even, displaying a message on the screen indicating the result.
#(EVEN MEANS NÚMERO PAR)
#(ODD MEANS NÚMERO IMPAR)
integer = int(input("Enter an integer: "))
if integer % 2 == 0:
  print("The number is even.")
else:
  print("The number is odd")

#SECOND EXCERCISE: 
#Create a function that receives a number and shows the previous and next number:
def show_previous_next(number):
  print("Previous number:", number - 1)
  print("Next number:", number + 1)
show_previous_next(5)

#THIRD EXCERCISE:
# Print from a certain range of numbers
# Print the number you receive (input) and the next 10 numbers
def number_range():
  start=int(input("Enter the start of the range"))
  end=int(input("Enter the end of the range"))
  for i in range(start, end + 1)
  print(i)
print(number_range)

#FOURTH EXCERCISE:
# Create a program that asks for the name and last name separately and prints "Last Name, First Name"
lastName = input("Enter your last name: ")
name = input("Enter your name: ")
#print(lastName + ", " + name)
print("{}, {}". format(lastName, name)) 
#That is, within each brace goes the following information: first brace: last name, second: first name.
#The newest and most standardized way:
print(f"{lastName}, {name}")
