from numb3rs import validate


def test_validate():
	assert validate('0.0.0.0') == True
	assert validate('255.255.255.255') == True
	assert validate('127.0.0.1') == True

	assert validate('256.256.256.256') == False
	assert validate('512.512.512.512') == False
	assert validate('1.2.3.1000') == False
	assert validate('-1.1.1.1') == False
	assert validate('1.2.3') == False
	assert validate('1.2.3.4.5') == False
	assert validate('cat') == False
