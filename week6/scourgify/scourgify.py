import sys
import os.path
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    input, output = sys.argv[1], sys.argv[2]
    if get_extension(input) != '.csv':
        sys.exit('Input is not a CSV file')
    if get_extension(output) != '.csv':
        sys.exit('Output is not a CSV file')
    if not os.path.isfile(input):
        sys.exit(f'Could not read {input}')
    if os.path.isfile(output):
        sys.exit(f'Cannot overwrite contents of a file. File {
            output} already exists'
        )
    scourgify(input, output)


def get_extension(file):
    return os.path.splitext(file)[1].lower()


def scourgify(input, output):
    with open(input) as input, open(output, 'w') as output:
        reader = csv.DictReader(input)
        writer = csv.DictWriter(output, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for row in reader:
            last, first = row['name'].split(', ')
            writer.writerow(
                {'first': first, 'last': last, 'house': row['house']}
            )


if __name__ == '__main__':
    main()
