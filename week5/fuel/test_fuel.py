import pytest
from fuel import convert, gauge


def test_convert():
    assert convert('0/4') == 0
    assert convert('1/4') == 25
    assert convert('1/2') == 50
    assert convert('3/4') == 75
    assert convert('1/1') == 100
    with pytest.raises(ValueError):
        convert('cat/dog')
        convert('2/1')
    with pytest.raises(ZeroDivisionError):
        convert('0/0')


def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'
    assert gauge(75) == '75%'
