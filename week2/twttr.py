def main():
    str = input('Input: ')
    res = ''
    for char in str:
        if not is_vowel(char):
            res += char
    print('Output:', res)


def is_vowel(char):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return char.lower() in vowels


if __name__ == '__main__':
    main()
