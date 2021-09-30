# Exercise 6: Rewrite the program that prompts the user for a list of
# numbers and prints out the maximum and minimum of the numbers at
# the end when the user enters “done”. Write the program to store the
# numbers the user enters in a list and use the max() and min() functions to
# compute the maximum and minimum numbers after the loop completes.

t = list()

while True:
    n = input('Enter a number: ')
    
    if n == 'done':
        break
    
    try:
        n = float(n)
    except:
        print('Invalid input')
        continue
    
    t.append(n)

print('Maximum: ', max(t))
print('Minimum: ', min(t))