from um import count


def test_um():
	assert count('um') == 1
	assert count('um um um') == 3
	assert count('umumum') == 0
	assert count('ummm') == 0
	assert count('yummy') == 0
	assert count('yum') == 0
	assert count('umbrella') == 0


def test_case_sensitivity():
	assert count('um') == 1
	assert count('UM') == 1
	assert count('Um') == 1
	assert count('uM') == 1


def test_around_punctuation():
	assert count('um?') == 1
	assert count('um!') == 1
	assert count('um...') == 1
	assert count('...um') == 1
	assert count('um, regular, um, expressions, um.') == 3
