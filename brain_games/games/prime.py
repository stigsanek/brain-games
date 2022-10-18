from brain_games.games.base import get_random_num, run_base_logic
from brain_games.games.const import ANSWER_YES, ANSWER_NO


def is_prime(number: int) -> bool:
    """
    Checks if a number is prime

    :param number: random number
    :return: bool
    """
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                return False

        else:
            return True

    return False


def get_answer(number: int) -> str:
    """
    Returns correct answer

    :param number: random number
    :return: str
    """
    return ANSWER_YES if is_prime(number) else ANSWER_NO


def run_prime():
    """
    Runs game logic

    :return:
    """
    game_text = f'Answer "{ANSWER_YES}" if given number is prime. ' \
                f'Otherwise answer "{ANSWER_NO}".'

    run_base_logic(
        game_text=game_text,
        question_fn=get_random_num,
        answer_fn=get_answer
    )
