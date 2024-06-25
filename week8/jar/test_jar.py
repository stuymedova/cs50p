from jar import Jar
import pytest


def test_jar():
    with pytest.raises(ValueError):
        Jar(-1)
    try:
        Jar()
    except Exception:
        raise pytest.fail('Unexpected error')
    jar1 = Jar(0)
    assert jar1.capacity == 0, jar1.size == 0
    jar2 = Jar(12)
    assert jar2.capacity == 12, jar2.size == 0


def test_deposit():
    jar = Jar(12)
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(3)
    jar.deposit(2)
    assert jar.size == 12


def test_withdraw():
    jar = Jar(12)
    jar.deposit(12)
    jar.withdraw(10)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)
    jar.withdraw(2)
    assert jar.size == 0


def test_str():
    jar = Jar(5)
    assert str(jar) == ''
    jar.deposit(1)
    assert str(jar) == '🍪'
    jar.deposit(4)
    assert str(jar) == '🍪🍪🍪🍪🍪'
    jar.withdraw(2)
    assert str(jar) == '🍪🍪🍪'
