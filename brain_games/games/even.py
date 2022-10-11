from brain_games.games.const import ANSWER_YES, ANSWER_NO


def get_game_text() -> str:
    """
    Returns condition game text

    :return: str
    """
    return f"Answer '{ANSWER_YES}' if the number is even, " \
           f"otherwise answer '{ANSWER_NO}'."


def get_answer(number: int) -> str:
    """
    Returns correct answer

    :param number: random number
    :return: str
    """
    return ANSWER_YES if number % 2 == 0 else ANSWER_NO
