"""The module contains functions that are used in all games"""
import prompt


def greet_user():
    """
    Greets user and returns username

    :return: str
    """
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    return user_name


def ask_question(question) -> str:
    """
    Ask a question user

    :param question: question for the user
    :return: str
    """
    answer = prompt.string(f"Question: {question}\nYour answer: ", empty=True)
    return str(answer)
