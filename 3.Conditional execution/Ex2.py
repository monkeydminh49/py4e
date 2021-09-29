hours = input('Enter Hours: ')

try:
    hours = float(hours)
except:
    print('Error, please enter numeric input')
    quit()

rate = input('Enter Rate: ')
try:
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    quit()
bonus = 0

if hours > 40:
    bonus = (hours - 40)*rate*0.5

print('Pay: ', str(hours*rate+bonus))
