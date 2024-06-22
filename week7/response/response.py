from validator_collection import is_email


def main():
    str = input('What\'s your email address: ')
    print('Valid' if is_email(str) else 'Invalid')


if __name__ == '__main__':
    main()
 