#!/usr/bin/env python3
from brain_games.games.base import get_random_num, run_base_logic
from brain_games.games.brain_even import get_game_text, get_answer


def main():
    """
    Main function

    :return:
    """
    run_base_logic(
        game_text=get_game_text(),
        question_fn=get_random_num,
        answer_fn=get_answer
    )


if __name__ == "__main__":
    main()
