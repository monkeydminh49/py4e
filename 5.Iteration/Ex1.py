# #Exercise 1: Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.

count = 0
sum = 0

while True:
    n = input('Enter a number: ')

    if n == 'done':
        break

    try:
        n = int(n)
    except:
        print('Invalid input')
        continue

    count = count + 1
    sum = sum + n


print(count, sum, sum/count)
