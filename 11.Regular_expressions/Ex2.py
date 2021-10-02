# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772

# Extract the number from each of the lines using a regular expression
# and the findall() method. Compute the average of the numbers and
# print out the average as an integer.

# Enter file:mbox.txt
# 38549

# Enter file:mbox-short.txt
# 39756


import re
numb = []

handle = open(input('Enter a file name: '))

for line in handle:
    line = line.rstrip()
    num = re.findall('^New Revision: ([0-9]+)$', line)
    if len(num) == 0: continue
    n = int(num[0])
    numb.append(n)

print(int(sum(numb)/len(numb)))

