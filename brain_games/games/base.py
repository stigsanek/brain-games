"""The module contains functions and constants that are used in all games"""
import random

import prompt

# Number of attempts in the game
ATTEMPT_COUNT = 3

# Range start number
NUMS_RANGE = (1, 100)


def get_random_num() -> int:
    """
    Returns random number from range

    :return:
    """
    return random.randint(NUMS_RANGE[0], NUMS_RANGE[1])


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


def run_base_logic(game_text: str, question_fn, answer_fn):
    """
    Runs general games loigc

    :param game_text: condition game text
    :param question_fn: fn that returns question (should not take arguments)
    :param answer_fn: fn that returns correct answer
    (must take one argument - result question_fn)
    :return:
    """
    user_name = greet_user()
    print(game_text)

    i = 0

    while i < ATTEMPT_COUNT:
        question = question_fn()
        correct_answer = answer_fn(question)

        answer = ask_question(question)

        if correct_answer != answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            break

        print("Correct!")
        i += 1

    if i == ATTEMPT_COUNT:
        print(f"Congratulations, {user_name}!")
    else:
        print(f"Let's try again, {user_name}!")
