# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
# Write a program that reads the words in words.txt and stores them as
# keys in a dictionary. It doesn’t matter what the values are. Then you
# can use the in operator as a fast way to check whether a string is in the
# dictionary.

import random


handle = open('words.txt')
di = {}

for lines in handle:
    words = lines.split()
    for word in words:
        di[word] = random.randint(0, 1000)

print(di)
print('the' in di)

