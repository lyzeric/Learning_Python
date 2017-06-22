print(r'c"\saf\asf\asf' '\\')
print(u'Hello sf')

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

endings = ['st' , 'nd' , 'rd'] + 17 * ['th'] \
        + ['st' , 'nd' , 'rd'] + 7 * ['th'] \
        + ['st']

year = input('Year :')
month = input('Month(1-12) :')
day = input('Day(1-31):')
month_number = int(month)
day_number = int(day)

month_number = months[month_number - 1]
oridinal = day + endings[day_number -1]

print(month_number + ' ' + oridinal + ' . ' + year)