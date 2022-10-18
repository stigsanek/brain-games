from brain_games.games.even import is_even


def test_is_even():
    """
    Test for is_even function

    :return:
    """
    assert is_even(10)
    assert not is_even(3)
