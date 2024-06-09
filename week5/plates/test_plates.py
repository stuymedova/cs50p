from plates import is_valid


def test_plates():
	assert is_valid('HELLO') == True
	assert is_valid('CS50') == True


def test_non_alphanum():
	assert is_valid('HELLO, WORLD') == False
	assert is_valid('PI3.14') == False


def test_invalid_length():
	assert is_valid('H') == False
	assert is_valid('GOODBYE') == False


def test_invalid_digits():
	assert is_valid('CS50P') == False
	assert is_valid('CS05') == False
	assert is_valid('50') == False
