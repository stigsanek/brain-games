import math

from brain_games.games.base import get_random_num


def get_game_text() -> str:
    """
    Returns condition game text

    :return: str
    """
    return "Find the greatest common divisor of given numbers."


def get_random_nums() -> str:
    """
    Returns two random numbers

    :return: str
    """
    num_one = get_random_num()
    num_two = get_random_num()

    return f"{num_one} {num_two}"


def get_answer(nums: str) -> str:
    """
    Returns correct answer

    :param nums: random nums
    :return: str
    """
    data = nums.split(" ")
    num_one = int(data[0])
    num_two = int(data[1])

    return str(math.gcd(num_one, num_two))
