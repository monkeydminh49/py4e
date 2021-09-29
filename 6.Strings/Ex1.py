# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.

fruit = 'banana'
index = len(fruit)

while index > 0 and index <= len(fruit):
    print(fruit[index-1])
    index -= 1
