#!/usr/bin/env python3
from brain_games.games.base import run_base_logic
from brain_games.games.brain_calc import get_answer
from brain_games.games.brain_calc import get_game_text, get_random_expr


def main():
    """
    Main function

    :return:
    """
    run_base_logic(
        game_text=get_game_text(),
        question_fn=get_random_expr,
        answer_fn=get_answer
    )


if __name__ == "__main__":
    main()
