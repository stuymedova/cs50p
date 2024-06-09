def main():
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
    while True:
        date = input('Date: ')
        try:
            if '/' in date:
                month, day, year = date.split('/')
                month, day, year = int(month), int(day), int(year)
            else:
                month_and_day, year = date.split(', ')
                month, day = month_and_day.split(' ')
                month = months.index(month) + 1
                day, year = int(day), int(year)
            if month > 12 or day > 31:
                raise Exception('Invalid date')
        except (ValueError, Exception, KeyError):
            pass
        else:
            print(f'{year:04}-{month:02}-{day:02}')
            break


main()
