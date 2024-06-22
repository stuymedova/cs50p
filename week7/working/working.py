import re


def main():
    str = input('Hours: ')
    print(convert(str))


def convert(str):
    time_regex = r'(\d{1,2})(?::(\d{2}))? (AM|PM)'
    matches = re.search(fr'^{time_regex} to {time_regex}$', str)
    if not matches:
        raise ValueError()
    start_hr, start_min, start_abbr, end_hr, end_min, end_abbr = matches.groups()
    start_hr, start_min = convert_time(int(start_hr), int(start_min or 0), start_abbr)
    end_hr, end_min = convert_time(int(end_hr), int(end_min or 0), end_abbr)
    return f'{start_hr:02}:{start_min:02} to {end_hr:02}:{end_min:02}'


def convert_time(hr: int, min: int, abbr: str) -> tuple[int, int]:
    if hr < 1 or hr > 12 or min < 0 or min > 59:
        raise ValueError()
    if hr == 12:
        hr = 0 if abbr == 'AM' else 12
    else:
        hr = hr if abbr == 'AM' else hr + 12
    return hr, min


if __name__ == '__main__':
    main()
