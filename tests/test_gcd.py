import pytest

from brain_games.games.gcd import get_random_nums, get_answer


def test_get_random_nums():
    """
    Test for get_random_nums function

    :return:
    """
    nums = get_random_nums().split(" ")

    assert isinstance(int(nums[0]), int)
    assert isinstance(int(nums[1]), int)


def test_get_answer():
    """
    Test for get_answer function

    :return:
    """
    assert get_answer("2 10") == "2"

    with pytest.raises(ValueError):
        get_answer("")
        get_answer("10 ")
