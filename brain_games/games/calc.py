import random

from brain_games.games.base import get_random_num
from brain_games.games.const import OPERATORS


def get_game_text() -> str:
    """
    Returns condition game text

    :return: str
    """
    return "What is the result of the expression?"


def get_random_expr() -> str:
    """Returns random expression"""
    symbols = list(OPERATORS.keys())

    idx = random.randint(0, len(symbols) - 1)
    num_one = get_random_num()
    num_two = get_random_num()

    return f"{num_one} {symbols[idx]} {num_two}"


def get_answer(expression: str) -> str:
    """
    Returns correct answer

    :param expression: random expression
    :return: str
    """
    data = expression.split(" ")
    fn = OPERATORS.get(data[1])
    num_one = int(data[0])
    num_two = int(data[2])

    return str(fn(num_one, num_two))
