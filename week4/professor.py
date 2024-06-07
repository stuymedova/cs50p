import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        sum = x + y
        for i in range(3):
            res = input(f'{x} + {y} = ')
            if res.isnumeric() and int(res) == sum:
                score += 1
                break
            elif i == 2:
                print(sum)
            else:
                print('EEE')
    print(f'Score: {score}')


def get_positive_int(prompt):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            pass
        else:
            if num > 0:
                return num


def get_level():
    while True:
        level = get_positive_int('Level: ')
        if 1 <= level <= 3:
            return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)
    raise ValueError


if __name__ == '__main__':
    main()
