from brain_games.games.base import get_random_num


def test_get_random_num():
    """
    Test for get_random_num function

    :return:
    """
    random_num = get_random_num()
    assert isinstance(random_num, int)
