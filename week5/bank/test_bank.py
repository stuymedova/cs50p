from bank import value


def test_value_is_zero():
    assert value('Hello, David') == 0
    assert value('hello') == 0


def test_value_is_twenty():
    assert value('Hey') == 20
    assert value('hi there') == 20


def test_value_is_one_hundred():
    assert value('What\'s up?') == 100
    assert value('good morning') == 100
