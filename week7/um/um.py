import re


def main():
    str = input('Input: ')
    print(count(str))


def count(str):
    matches = re.findall(r'\bum\b', str, re.IGNORECASE)
    return len(matches)


if __name__ == '__main__':
    main()
