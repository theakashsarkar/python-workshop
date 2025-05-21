from pytest import mark
from message import show_count

@mark.parametrize('qty, expected', [
    (1, '1 part'),
    (2, '2 parts'),
])

def test_show_count(qty, expected):
    got = show_count(qty)
    assert got == expected

def test_show_count_zero():
    got = show_count(0)
    assert got == 'no parts'

def test_irregular() -> None:
    got = show_count(2,'mouse', 'mice')
    assert got == '2 mouse'
