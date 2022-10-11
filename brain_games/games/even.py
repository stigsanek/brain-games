from brain_games.games.base import get_random_num, run_base_logic
from brain_games.games.const import ANSWER_YES, ANSWER_NO


def get_answer(number: int) -> str:
    """
    Returns correct answer

    :param number: random number
    :return: str
    """
    return ANSWER_YES if number % 2 == 0 else ANSWER_NO


def run_even():
    """
    Runs game logic

    :return:
    """
    game_text = f'Answer "{ANSWER_YES}" if the number is even, ' \
                f'otherwise answer "{ANSWER_NO}".'

    run_base_logic(
        game_text=game_text,
        question_fn=get_random_num,
        answer_fn=get_answer
    )
