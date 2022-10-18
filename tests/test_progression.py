import pytest

from brain_games.games.const import HIDDEN_EL, PROGRESSION_LEN
from brain_games.games.progression import get_answer
from brain_games.games.progression import get_progression, calculate_step


def test_get_progression():
    """
    Test for get_progression function

    :return:
    """
    data = get_progression().replace(HIDDEN_EL, "").replace("  ", " ").strip()
    numbers = list(map(lambda x: int(x), data.split(" ")))

    assert len(numbers) == PROGRESSION_LEN - 1


def test_calculate_step():
    """
    Test for calculate_step function

    :return:
    """
    assert calculate_step([]) == 0
    assert calculate_step([2, 4, 6]) == 2
    assert calculate_step([2]) == 0


def test_get_answer():
    """
    Test for get_answer function

    :return:
    """
    assert get_answer(".. 4 6 8 10 12") == "2"
    assert get_answer("2 4 6 .. 10 12") == "8"
    assert get_answer("2 4 6 8 10 ..") == "12"
    assert get_answer("2 4 ..") == "6"

    with pytest.raises(ValueError):
        get_answer("2 ..")
