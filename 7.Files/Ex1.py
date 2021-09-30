# Exercise 1: Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. Executing the program will
# look as follows:

fout = open(input('Enter a file name: '))

for i in fout:
    print(i.upper())