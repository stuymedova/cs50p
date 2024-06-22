import re


def main():
    str = input('HTML: ')
    print(parse(str))


def parse(str):
    yt_embed_regex = r'<iframe .*src="https?://(?:www\.)youtube\.com/embed/(\w+)".*></iframe>'
    matches = re.search(yt_embed_regex, str)
    return matches.group(1) if matches else None


if __name__ == '__main__':
    main()
