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
