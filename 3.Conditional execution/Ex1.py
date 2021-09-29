hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
bonus = 0

if hours > 40:
    bonus = (hours - 40)*rate*0.5

print('Pay: ', str(hours*rate+bonus))