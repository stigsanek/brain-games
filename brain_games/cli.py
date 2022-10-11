import prompt


def welcome_user() -> str:
    """
    Performs a user greeting

    :return: str
    """
    return prompt.string("May I have your name? ")
