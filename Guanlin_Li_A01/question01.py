#Course: PROG8420-20F-Sec1-Programming for Big Data
#Assignment Number: Assignment_1
#Creation Date: 2020.09.16
#Author: Guanlin Li
#StudentID: 8674601

import math  # import math library in order to use function factorial().
number = input("Please enter a number: ")  # input a number from keyboard.
# if the input is only include numbers
while number.isdigit() == False:
  number = input("Invalid Number. Please enter a number: ")
else:
  print("Your number is: ", number)
factorial = math.factorial(int(number))  # because the input from keyboard is a string,
                                         # it needs to be transferred to an integer, then calculate the factorial.
print("The factorial of", number, "is",factorial)  # print result out
