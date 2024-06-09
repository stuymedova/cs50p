from twttr import shorten


def test_shorten():
    assert shorten('Hello, world!') == 'Hll, wrld!'
    assert shorten('') == ''
    assert shorten('aeiou') == ''
    assert shorten('AEIOU') == ''
    assert shorten('bcdfghjklmnpqrstvwxyz') == 'bcdfghjklmnpqrstvwxyz'
    assert shorten('BCDFGHJKLMNPQRSTVWXYZ') == 'BCDFGHJKLMNPQRSTVWXYZ'
