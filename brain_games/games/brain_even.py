from brain_games.games.base import get_random_num, run_base_logic

# Correct answer
ANSWER_YES = "yes"

# Wrong Answer
ANSWER_NO = "no"


def get_correct_answer(number: int) -> str:
    """
    Returns correct answer

    :param number: random number
    :return: str
    """
    return ANSWER_YES if number % 2 == 0 else ANSWER_NO


def run_brain_even():
    """
    Runs game logic

    :return:
    """
    game_text = f"Answer '{ANSWER_YES}' if the number is even, " \
                f"otherwise answer '{ANSWER_NO}'."

    run_base_logic(
        game_text=game_text,
        question_fn=get_random_num,
        answer_fn=get_correct_answer
    )
