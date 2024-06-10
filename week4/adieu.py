import inflect


def main():
    prefix = 'Adieu, adieu, to '
    names = []
    while True:
        try:
            name = input('Name: ')
            names.append(name)
        except EOFError:
            break
    if len(names) == 1:
        print(prefix + names[0])
    else:
        p = inflect.engine()
        print(prefix + p.join(names))


if __name__ == '__main__':
    main()
