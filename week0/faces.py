def main():
	str = input()
	str = convert(str)
	print(str)


def convert(str):
	return str.replace(':)', '🙂').replace(':(', '🙁')


if __name__ == '__main__':
	main()
