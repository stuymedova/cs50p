def main():
    str = input('Input: ')
    print('Output:', shorten(str))


def shorten(str):
    res = ''
    for char in str:
        if not is_vowel(char):
            res += char
    return res


def is_vowel(char):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return char.lower() in vowels


if __name__ == '__main__':
    main()
