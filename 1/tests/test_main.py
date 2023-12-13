from src.main import (add_first_and_last_digit, get_all_digits, get_digit,
                      get_first_digit, get_last_digit, get_number_of_digits)


def test_get_digit_with_digit():
    expected = 1
    actual = get_digit(1)
    assert expected == actual


def test_get_digit_with_character():
    expected = None
    actual = get_digit("w")
    assert expected == actual


def test_get_all_digits():
    expected = [1, 2]
    actual = get_all_digits("te1st2")
    assert expected == actual


def test_get_first_digit():
    expected = 7
    actual = get_first_digit("7jlncfksix7rjgrpglmn9")
    assert expected == actual


def test_get_last_digit():
    expected = 9
    actual = get_last_digit("7jlncfksix7rjgrpglmn9")
    assert expected == actual


def test_get_number_of_digits():
    expected = 3
    digits = get_all_digits("te1st22")
    actual = get_number_of_digits(digits)
    assert expected == actual


def test_add_first_and_last_digit():
    expected = 38
    actual = add_first_and_last_digit("pqr3stu8vwx")
    assert expected == actual
