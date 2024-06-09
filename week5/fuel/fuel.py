def main():
    while True:
        try:
            percentage = convert(input('Fraction: '))
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split('/')
    x, y = int(x), int(y)
    if x > y:
        raise ValueError('X must be less that Y')
    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    if percentage >= 99:
        return 'F'
    return f'{percentage}%'


if __name__ == '__main__':
    main()
