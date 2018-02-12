import sys
day_seq = 0
day_in_month = [31,28,31,30,31,30,31,30,30,31,30,31]

month = input('Enter month: ')
if (month>12) or (month<1):
    print 'Month incorrect'
    sys.exit()
    
date = input('Enter date: ')

if (date>day_in_month[month-1]) or (date<1):
    print 'date incorrect'
    sys.exit()

for i in range (0, month-1):
    day_seq += day_in_month[i]
print 'Day sequence is %d' % (day_seq+date)
