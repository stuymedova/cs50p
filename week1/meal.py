def main():
	time = input('What time is it? ')
	time_in_fractions = convert(time)
	if time_in_fractions >= 7 and time_in_fractions <= 8:
		print('breakfast time')
	elif time_in_fractions >= 12 and time_in_fractions <= 13:
		print('lunch time')
	elif time_in_fractions >= 18 and time_in_fractions <= 19:
		print('dinner time')


def convert(time):
	hours, minutes = time.split(':')
	hours, minutes = int(hours), int(minutes)
	min_in_fractions = minutes / 60
	return float(hours + min_in_fractions)


if __name__ == '__main__':
	main()
