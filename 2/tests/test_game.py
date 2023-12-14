import pytest
from src.Game import Game


@pytest.fixture
def game():
    return Game(1)


def test_init_game():
    random = Game(1)
    expected = []
    actual = random.rounds
    assert expected == actual


def test_add_round(game):
    game.add_round("3 blue, 4 red")
    expected = ["3 blue, 4 red"]
    actual = game.rounds
    assert expected == actual


def test_round_is_valid(game):
    expected = True
    game.add_round("3 blue, 4 red")
    round = game.rounds[0]
    actual = game.round_is_valid(round)
    assert expected == actual


def test_round_is_invalid(game):
    expected = False
    game.add_round("15 blue, 4 red")
    round = game.rounds[0]
    actual = game.round_is_valid(round)
    assert expected == actual


def test_game_valid(game):
    expected = True
    game.add_round("3 blue, 4 red")
    game.add_round("5 blue, 9 red")
    actual = game.game_is_valid()
    assert expected == actual


def test_game_invalid(game):
    expected = False
    game.add_round("3 blue, 4 red")
    game.add_round("9 blue, 19 red")
    actual = game.game_is_valid()
    assert expected == actual
