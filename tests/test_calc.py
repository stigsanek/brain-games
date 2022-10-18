import pytest

from brain_games.games.calc import get_random_expr, get_answer
from brain_games.games.const import OPERATORS


def test_get_random_expr():
    """
    Test for get_random_expr function

    :return:
    """
    expr = get_random_expr()
    num_one, operator, num_two = expr.split(" ")

    assert operator in OPERATORS
    assert isinstance(int(num_one), int)
    assert isinstance(int(num_two), int)


def test_get_answer():
    """
    Test for get_answer function

    :return:
    """
    assert get_answer("5 * 5") == "25"
    assert get_answer("10 - 20") == "-10"

    with pytest.raises(ValueError):
        get_answer("")
        get_answer("10 - ")
