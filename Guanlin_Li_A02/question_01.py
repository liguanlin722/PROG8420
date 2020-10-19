#Course: PROG8420-20F-Sec1-Programming for Big Data
#Assignment Number: Assignment_2
#Creation Date: 2020.09.29
#Author: Guanlin Li
#StudentID: 8674601

import random
from collections import Counter

# Imagine there are n dices, so the number of sum is 6**n.
# Imagine F(n, s). n means the number of dices, s means the times of sum
# When n = 1, the case for sum can be represented as F(n, s) = 1, s = 1, 2, ..., 6
# When n > 1, F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)
# The case for last dice equals the sum of all the cases before the lase one.

def twoSum( n: int):
  dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]
  for i in range(1, 7):
    dp[1][i] = 1

  for i in range(2, n + 1):
    for j in range(i, i * 6 + 1):
      for k in range(1, 7):
        if j >= k + 1:
          dp[i][j] += dp[i - 1][j - k]
  res = {}
  for i in range(n, n * 6 + 1):
    res.update({i: dp[n][i] * 1.0 / 6 ** n})
  return res

# dice = [1, 2, 3, 4, 5, 6]

numberOfDice = input('Please enter the number of dice(1 to 16): ')
while numberOfDice.isdigit() == False or int(numberOfDice) < 1 or int(numberOfDice) > 16:
  numberOfDice = input('Invalid Number. Please enter the number of dice(1 to 16): ')

numberOfRoll = input('Please enter the number of roll(1 or more): ')
while numberOfRoll.isdigit() == False or int(numberOfRoll) < 1:
  numberOfRoll = input('Invalid Number. Please enter the number of roll(1 or more): ')

number_of_roll = int(numberOfRoll)

dice_total_list = []
while number_of_roll != 0:
  dice_total = random.randint(1 * int(numberOfDice), 6 * int(numberOfDice))
  dice_total_list.append(dice_total)
  number_of_roll -= 1
else:
  print('The list of dice total: ', dice_total_list)

c = Counter(dice_total_list)
key=list(c.keys())
actual_percentage = {}
for a in key:
  actual_percentage.update({a: c[a]/int(numberOfRoll)})
print('The actual percentage of each total is: ', actual_percentage)
theoretical_percentage = twoSum(int(numberOfDice))
print('The theoretical percentage of each total is: ', twoSum(int(numberOfDice)))

error_percentage = {}
for b in key:
  error_percentage.update({b: actual_percentage[b] - theoretical_percentage[b]})
print('The error percentage of each total is: ', error_percentage)
