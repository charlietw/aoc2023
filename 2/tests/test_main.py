from src.main import get_id, get_rounds

def test_get_id():
    input = "Game 10: 1 blue, 1 red; 10 red; 8 red, 1 blue, 1 green; 1 green, 5 blue"
    expected = 10
    actual = get_id(input)
    assert expected == actual

def test_get_rounds():
    input = "Game 10: 1 blue, 1 red; 10 red; 8 red, 1 blue, 1 green; 1 green, 5 blue"
    expected = ["1 blue, 1 red", "10 red", "8 red, 1 blue, 1 green", "1 green, 5 blue"]
    actual = get_rounds(input)
    assert expected == actual
