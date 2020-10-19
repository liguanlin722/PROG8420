#Course: PROG8420-20F-Sec1-Programming for Big Data
#Assignment Number: Assignment_03
#Creation Date: 2020.10.13
#Author: Guanlin Li
#StudentID: 8674601

L = []  # Create a list to keep the numbers.
for i in range(2, 1001):  # In order to check the value between 2 and 1000, we need to start at 2, end with 1001.
  k = 0
  for j in range(1, i):
    if (i % j == 0):
      k += j
  if i == k:
    L.append(i)
print(L)
