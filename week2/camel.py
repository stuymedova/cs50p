def main():
    str = input('camelCase: ')
    res = ''
    for char in str:
        if char.isupper():
            res += f'_{char.lower()}'
        else:
            res += char
    print('snake_case:', res)


if __name__ == '__main__':
    main()
