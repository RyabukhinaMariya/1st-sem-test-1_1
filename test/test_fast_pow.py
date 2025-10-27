from src.fast_pow import fastPow


def test_two_power_two():
    assert fastPow(2, 2) == 4


def test_negative():
    assert fastPow(-1, 4) == 1


def test neg_pow():
    assert fastPow(2, -1) == 0.5


def test zero_pow():
    assert fastPow(2, 0) == 1
