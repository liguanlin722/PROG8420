#Course: PROG8420-20F-Sec1-Programming for Big Data
#Assignment Number: Assignment_2
#Creation Date: 2020.09.29
#Author: Guanlin Li
#StudentID: 8674601

from collections import Counter

p = input('Please enter a paragraph: ')

p_str = str(p)

P = p_str.upper()

print(P)
words = []  # create a empty list
index = 0  # go through all the characters in paragraph
start = 0  # record the beginning of each word
while index < len(P):
  start = index  # reset the start point for each word
  while P[index] != " " and P[index] not in [".", ","]:
    index += 1
    if index == len(P):  # if the index is finished
      break
  words.append(P[start:index])
  if index == len(P):
    break
  while P[index] == " " or P[index] in [".", ","]:
    index += 1
    if index == len(P):
      break

print(words)

a = Counter(words)

for k in sorted(a):
  print(k,':', a[k])
