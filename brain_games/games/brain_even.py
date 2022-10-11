import random

from brain_games.games.const import ATTEMPT_COUNT
from brain_games.games.func import greet_user, ask_question

# Range start number
RAND_INT_START = 1

# Range end number
RAND_INT_END = 100

# Correct answer
ANSWER_YES = "yes"

# Wrong Answer
ANSWER_NO = "no"


def run_brain_even():
    """
    Runs game logic

    :return:
    """
    user_name = greet_user()
    print(f"Answer '{ANSWER_YES}' if the number is even, "
          f"otherwise answer '{ANSWER_NO}'.")

    i = 0

    while i < ATTEMPT_COUNT:
        number = random.randint(RAND_INT_START, RAND_INT_END)

        correct_answer = ANSWER_YES if number % 2 == 0 else ANSWER_NO
        answer = ask_question(number)

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
