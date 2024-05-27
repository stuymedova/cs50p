def main():
	str = input()
	str = convert(str)
	print(str)


def convert(str):
	return str.replace(':)', '🙂').replace(':(', '🙁')


main()
