import random

from brain_games.games.base import get_random_num, run_base_logic
from brain_games.games.const import PROGRESSION_LEN, HIDDEN_EL


def get_progression() -> str:
    """
    Returns progression

    :return: str
    """
    start_num = get_random_num()
    step = random.randint(1, PROGRESSION_LEN)
    data = []

    for i in range(0, PROGRESSION_LEN):
        data.append(str(start_num))
        start_num = start_num + step

    data[step - 1] = HIDDEN_EL

    return " ".join(data)


def calculate_step(nums: list) -> int:
    """
    Calculate progression step

    :param nums:
    :return:
    """
    step = 0

    for i in range(0, len(nums) - 1):
        min_step = nums[i + 1] - nums[i]

        if not step or step > min_step:
            step = min_step

    return step


def get_answer(progression: str) -> str:
    """
    Returns correct answer

    :param progression: nums progression
    :return: str
    """
    data = progression.split(" ")
    nums = []
    idx = 0

    for i in range(0, len(data)):
        try:
            nums.append(int(data[i]))
        except ValueError:
            idx = i

    step = calculate_step(nums)

    if idx == 0:
        return str(nums[idx] - step)

    return str(nums[idx - 1] + step)


def run_progression():
    """
    Runs game logic

    :return:
    """
    run_base_logic(
        game_text="What number is missing in the progression?",
        question_fn=get_progression,
        answer_fn=get_answer
    )
