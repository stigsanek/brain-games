from brain_games.games.prime import is_prime


def test_is_prime():
    """
    Test for is_prime function

    :return:
    """
    assert not is_prime(1)
    assert not is_prime(0)
    assert not is_prime(-100)
    assert is_prime(2)
    assert is_prime(97)
