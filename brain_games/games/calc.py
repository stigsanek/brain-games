import random

from brain_games.games.base import get_random_num, run_base_logic
from brain_games.games.const import OPERATORS


def get_random_expr() -> str:
    """
    Returns random expression

    :return: str
    """
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

    if len(data) != 3:
        raise ValueError(
            "The expression must contain two operands and one operator"
        )

    fn = OPERATORS.get(data[1])
    num_one = int(data[0])
    num_two = int(data[2])

    return str(fn(num_one, num_two))


def run_calc():
    """
    Runs game logic

    :return:
    """
    run_base_logic(
        game_text="What is the result of the expression?",
        question_fn=get_random_expr,
        answer_fn=get_answer
    )
