#Course: PROG8420-20F-Sec1-Programming for Big Data
#Assignment Number: Assignment_1
#Creation Date: 2020.09.16
#Author: Guanlin Li
#StudentID: 8674601

import math

def isdecimal(n):  # define a function to check if the number is a decimal.
  x = int(n)  # transfer the number into an integer forcibly, so that it will keep the integer part.
  result = n - x
  if result == 0:  # if the result is 0, that means the number is an integer, otherwise it's a decimal.
    return False
  else:
    return True
print("Plese separate each element by comma.")
numbers = input("Please enter a set of number: ")

while numbers == '' or numbers.isalpha() == True:  #if users input a space or a letter, let them enter again
  numbers = input("Invalid Number. Please enter a number: ")
else:
  print("Your numbers are: ", numbers)

numbers_list = []
for i in numbers.split(","):
  numbers_list.append(float(i))   #transfer all elements into float might be easier to calculate
j = 0
for k in numbers_list:
  if isdecimal(k) == False:
    j = j + 1
print("The amount of integer is ", j)
sum = math.fsum(numbers_list)
print("The sum of numbers is ", sum)
average = sum/len(numbers_list)
print("The average of numbers is ", average)

