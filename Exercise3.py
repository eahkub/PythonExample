import sys

day_seq = 0
day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

month = raw_input('Input month: ')

if (int(month)>12) or (int(month)<1):
    print 'In correct month.'
    sys.exit()

date = raw_input('Enter date: ')


if (int(date)>day_in_month[int(month)-1]) or int(date)<1:
    print 'Incorrect date.'
    sys.exit()

for x in range(0, int(month)-1):
    day_seq += day_in_month[x]

print 'Day sequence of the year is %d' % (int(day_seq)+int(date))
