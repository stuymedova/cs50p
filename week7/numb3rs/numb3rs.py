import re


def main():
    str = input('IPv4 Address: ')
    print(validate(str))


def validate(str):
    if matches := re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', str):
        ip_range = range(0, 256)
        return (int(matches.group(1)) in ip_range and
                int(matches.group(2)) in ip_range and
                int(matches.group(3)) in ip_range and
                int(matches.group(4)) in ip_range)
    return False


if __name__ == '__main__':
    main()
