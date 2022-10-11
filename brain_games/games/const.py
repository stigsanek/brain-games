import operator

# Number of attempts in the game
ATTEMPT_COUNT = 3

# Random number range
NUMS_RANGE = (1, 100)

# Correct answer
ANSWER_YES = "yes"

# Wrong Answer
ANSWER_NO = "no"

# Math operators map
OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul
}

# Progression length
PROGRESSION_LEN = 10

# Hidden number symbol
HIDDEN_EL = ".."
