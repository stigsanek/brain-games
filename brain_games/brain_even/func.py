import random

import prompt

from brain_games.brain_even.const import RAND_INT_START, RAND_INT_END


def get_number() -> int:
    """
    Generates a random number

    :return: int
    """
    return random.randint(RAND_INT_START, RAND_INT_END)


def ask_question(number: int) -> str:
    """
    Ask a question user

    :param number: random number
    :return: str
    """
    return str(prompt.string(f"Question: {number}\nYour answer: ", empty=True))


def is_even_num(number: int) -> bool:
    """
    Checks if a number is even

    :param number: random number
    :return: bool
    """
    return number % 2 == 0
