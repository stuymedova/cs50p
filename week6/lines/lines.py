import sys
import os.path


def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    file = sys.argv[1]
    if get_extension(file) != '.py':
        sys.exit('Not a Python file')
    if not os.path.isfile(file):
        sys.exit('File does not exist')
    with open(file) as file:
        loc_count = count_lines(file)
    print(loc_count)


def get_extension(file):
    return os.path.splitext(file)[1].lower()


def count_lines(text):
    loc_count = 0
    for line in text:
        line = line.lstrip()
        if len(line) == 0 or line.startswith('#'):
            continue
        loc_count += 1
    return loc_count


if __name__ == '__main__':
    main()
