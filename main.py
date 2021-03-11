###exercise 47 from ben stephenson's "the python workbook".
###the bit with creating an extra list of the first days is inelegant, but I don't have a better idea right now.

print('Enter the month and day:')
m, d = input().split(',')

this_month = m
day_of_month = int(d)
total_days = 0

first_days = {  20: 'Aquarius',
                50: 'Pisces',
                80: 'Aries',
                110: 'Taurus',
                141: 'Gemini',
                172: 'Cancer',
                204: 'Leo',
                235: 'Virgo',
                266: 'Libra',
                296: 'Scorpio',
                326: 'Sagittarius',
                356: 'Capricorn' }

list_of_first_days = [i for i in first_days.keys()]

monthdays = { 'january': 31,
              'february': 28,
              'march': 31,
              'april': 30,
              'may': 31,
              'june': 30,
              'july': 31,
              'august': 31,
              'september': 30,
              'october': 31,
              'november': 30,
              'december': 31 }

if this_month in monthdays.keys():
  if day_of_month > monthdays[this_month]:
    day_of_month = monthdays[this_month]


for i in monthdays.keys():
  total_days += monthdays[i]
  if i == this_month:
    total_days = total_days - monthdays[i] + day_of_month
    break


if total_days < 20 or total_days >= 356:
  sign = 'Capricorn'
else:
  for i in range(len(list_of_first_days)):
    if total_days >= list_of_first_days[i] and (total_days < list_of_first_days[i+1]):
      sign = first_days.get(list_of_first_days[i])

print(sign)
print(total_days)
