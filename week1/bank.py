def main():
	answer = input('Greeting: ').strip().lower()
	if answer.startswith('hello'):
		print('$0')
	elif answer.startswith('h'):
		print('$20')
	else:
		print('$100')


if __name__ == '__main__':
	main()
