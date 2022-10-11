from brain_games.brain_even.const import ATTEMPT_COUNT, ANSWER_YES, ANSWER_NO
from brain_games.brain_even.func import get_number, ask_question, is_even_num
from brain_games.func import greet_user


def run_logic():
    """
    Runs game logic

    :return:
    """
    user_name = greet_user()
    print(f"Answer '{ANSWER_YES}' if the number is even, "
          f"otherwise answer '{ANSWER_NO}'.")

    i = 0

    while i < ATTEMPT_COUNT:
        number = get_number()

        correct_answer = ANSWER_YES if is_even_num(number) else ANSWER_NO
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
