# Print out a date, given year, month, and day as number

# List of Months
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
    'December'
]

# A list with one ending for each number from 1 to 31

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
        + ['st', 'nd', 'rd'] +  7 * ['th'] \
        + ['st']

year    = input('Year: ')
month   = input('Month (1-12): ')
day     = input('Day (1-31): ')

month_number = int(month)
day_number   = int(day)

# Remember to substract 1 from month and day to get a correct index
month_name = months[month_number -1]
ordinal    = day + endings[day_number -1]

# Print result
print(month_name + ' ' + ordinal + ', ' + year)

# Prompt User to close program
input("\nPress 'Enter' to end program...")
