import random


def main():
	high = get_positive_int('Level: ')
	target = random.randint(1, high)
	while True:
		guess = get_positive_int('Guess: ')
		if guess < target:
			print('Too small!')
		elif guess > target:
			print('Too large!')
		else:
			print('Just right!')
			break


def get_positive_int(prompt):
	while True:
		try:
			num = int(input(prompt))
		except ValueError:
			pass
		else:
			if num > 0:
				return num


if __name__ == '__main__':
	main()
