# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(x):
    del x[0]
    del x[-1]

def middle(t):
    new = t[1:]
    del new[-1]
    return new

a = ['a', 'b', 'c', 'd', 'e', 'f']
b = [1, 2, 3, 4, 5, 6]

test = chop(a)
test1 = middle(b)

print(a)
print(test)

print(b)
print(test1)