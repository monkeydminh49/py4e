# Exercise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.
max = None
min = None

while True:
    n = input('Enter a number: ')
    
    if n == 'done':
        break
    
    try:
        n = int(n)
    except:
        print('Invalid input')
        continue
    
    if max is None or n > max:
        max = n
    if min is None or n < min:
        min = n

print(min, max)