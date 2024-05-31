def main():
	while True:
		try:
			x, y = input('Fraction: ').split('/')
			x, y = int(x), int(y)
			if x > y:
				raise Exception('X must be less that Y')
			res = round((x / y) * 100)
			break
		except (ValueError, Exception, ZeroDivisionError):
			pass
	if res <= 1:
		print('E')
	elif res >= 99:
		print('F')
	else:
		print(f'{res}%')


main()
