from tabulate import tabulate
import sys
import os.path
import csv


def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    file = sys.argv[1]
    if get_extension(file) != '.csv':
        sys.exit('Not a CSV file')
    if not os.path.isfile(file):
        sys.exit('File does not exist')
    with open(file) as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt='grid'))


def get_extension(file):
    return os.path.splitext(file)[1].lower()


if __name__ == '__main__':
    main()
