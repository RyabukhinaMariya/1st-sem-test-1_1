from src.luhn import luhnСheck


def test_good():
    assert luhnСheck("8571 2612 1234 5467")


def test_bad():
    assert not luhnСheck("4561 2612 1234 5463")


def test_empty_num():
    assert not luhnСheck("") == "Error"


def test_empty_num():
    assert not luhnСheck("qwerty") == "Error"
