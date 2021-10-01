# Exercise 3: Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages and see how
# letter frequency varies between languages. Compare your results with
# the tables at https://wikipedia.org/wiki/Letter_frequencies.


handle = open(input('Enter a file name: '))
d = {}

import string

for line in handle:
    line.rstrip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for let in word:
            d[let] = d.get(let, 0) + 1

ls = sorted([(v, k) for k, v in d.items()], reverse=True)

for v, k in ls:
    print(k, v)
