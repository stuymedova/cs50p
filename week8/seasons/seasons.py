import datetime
import inflect
import re
import sys


def main():
    date_of_birth = input('Date of Birth: ')
    try:
        age_in_min = int(get_age(date_of_birth) / 60)
    except ValueError as e:
        sys.exit(e)
    p = inflect.engine()
    age_in_words = p.number_to_words(age_in_min, andword='')
    print(f'{age_in_words.capitalize()} {p.plural('minute', age_in_min)}')


def get_age(date_of_birth: str) -> int:
    """Returns the number of seconds passed since the date of birth"""
    matches = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})', date_of_birth)
    if not matches:
        raise ValueError('Invalid date')
    year, month, day = map(lambda x: int(x), matches.groups())
    date_of_birth = datetime.date(year, month, day)
    today = datetime.date.today()
    return (today - date_of_birth).total_seconds()


if __name__ == '__main__':
    main()
