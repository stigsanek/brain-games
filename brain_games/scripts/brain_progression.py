#!/usr/bin/env python3
from brain_games.games.base import run_base_logic
from brain_games.games.progression import get_answer
from brain_games.games.progression import get_game_text, get_progression


def main():
    """
    Main function

    :return:
    """
    run_base_logic(
        game_text=get_game_text(),
        question_fn=get_progression,
        answer_fn=get_answer
    )


if __name__ == "__main__":
    main()
