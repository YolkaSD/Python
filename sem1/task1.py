import math

distDay = int(input('How much do you need to drive in a day: '))
distTotal = int(input('What distance do you need to travel: '))
#day = math.ceil(distTotal / distDay)
#day = (distTotal + distDay - 1) // distDay
day = distTotal // distDay + int(distTotal % distDay != 0)
print('Need {} days'.format(day))


