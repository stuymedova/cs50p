def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(plate):
    first_digit_index = find_first_digit(plate)
	# Appropriate length
    if len(plate) < 2 or len(plate) > 6:
        return False
    # Only letters and digits
    if not plate.isalnum():
        return False
    if first_digit_index is not None:
        # Start with at least two letters
        if first_digit_index < 2:
            return False
        # First number cannot be a zero
        if plate[first_digit_index] == '0':
            return False
        # Numbers must come at the end
        if not are_digits(plate, first_digit_index, len(plate)):
            return False
    return True


def find_first_digit(str):
    for i in range(len(str)):
        if str[i].isdigit():
            return i
    return None


def are_digits(str, start, end):
    for i in range(start, end):
        if not str[i].isdigit():
            return False
    return True


if __name__ == '__main__':
    main()
