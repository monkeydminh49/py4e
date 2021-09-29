def computerpay(hours, rate):
    try:
        hours = int(hours)
    except:
        print('Error, please enter numeric input')
        quit()

    try:
        rate = int(rate)
    except:
        print('Error, please enter numeric input')
        quit()

    bonus = 0
    
    print('Enter Hours: ', hours)
    print('Enter Rate: ', rate)

    if hours > 40:
        bonus = (hours - 40)*rate*0.5

    print('Pay: ', str(hours*rate+bonus))

computerpay(45,10)