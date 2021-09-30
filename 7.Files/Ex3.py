# Exercise 3: Sometimes when programmers get bored or want to have a
# bit of fun, they add a harmless Easter Egg to their program. Modify
# the program that prompts the user for the file name so that it prints a
# funny message when the user types in the exact file name “na na boo
# boo”. The program should behave normally for all other files which
# exist and don’t exist. Here is a sample execution of the program:


file_name = input('Enter the file name: ')
count = 0

if file_name == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    exit()
try:
    open_file = open(file_name)
except:
    print('File cannot be opened: ', file_name)
    exit()

for i in open_file:
    if i.startswith('Subject:'):
        count += 1

print('There were ', count, 'subject lines in ', file_name)

