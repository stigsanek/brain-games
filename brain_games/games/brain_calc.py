import operator
import random

from brain_games.games.base import get_random_num, run_base_logic

# Math operators map
OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}


def get_random_expression() -> str:
    """Returns random expression"""
    symbols = list(OPERATORS.keys())

    idx = random.randint(0, len(symbols) - 1)
    num_one = get_random_num()
    num_two = get_random_num()

    return f"{num_one} {symbols[idx]} {num_two}"


def get_correct_answer(expression: str) -> str:
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


def run_brain_calc():
    """
    Runs game logic

    :return:
    """
    game_text = "What is the result of the expression?"

    run_base_logic(
        game_text=game_text,
        question_fn=get_random_expression,
        answer_fn=get_correct_answer
    )
