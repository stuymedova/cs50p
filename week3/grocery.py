def main():
    dict = {}
    while True:
        try:
            str = input().strip().upper()
            if str in dict:
                dict[str] += 1
            else:
                dict[str] = 1
        except EOFError:
            break
    sorted_keys = sorted(dict.keys())
    for key in sorted_keys:
        print(dict[key], key)


main()
