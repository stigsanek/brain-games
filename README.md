# Brain games

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/stigsanek/brain-games/pyci.yml?branch=main)
![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/stigsanek/brain-games)
![Code Climate coverage](https://img.shields.io/codeclimate/coverage/stigsanek/brain-games)

## Description

"Brain games" is a set of five console games based on the popular mobile brain-pumping apps. Each game asks questions
that need to be answered correctly. After three correct answers, the game is considered completed. Incorrect answers end
the game and prompt you to play it again. Games:

* Calculator. Arithmetic expressions to be calculated.
* Progression. Finding missing numbers in a sequence of numbers.
* Determining an even number.
* Determining the largest common divisor.
* Determining a prime number.

## Install

### Python

Before installing the package, you need to make sure that you have Python version 3.8 or higher installed.

```bash
>> python --version
Python 3.8.0+
```

If you don't have Python installed, you can download and install it
from [the official Python website](https://www.python.org/downloads/).

### Poetry

The project uses the Poetry manager. Poetry is a tool for dependency management and packaging in Python. It allows you
to declare the libraries your project depends on and it will manage (install/update) them for you. You can read more
about this tool on [the official Poetry website](https://python-poetry.org/)

### Package

To work with the package, you need to clone the repository to your computer. This is done using the `git clone` command.
Clone the project on the command line:

```bash
# clone via HTTPS:
>> git clone https://github.com/stigsanek/brain-games.git
# clone via SSH:
>> git@github.com:stigsanek/brain-games.git
```

It remains to move to the directory and install the package:

```bash
>> cd brain-games
>> poetry build
>> python -m pip install --user dist/*.whl
```

Finally, we can move on to using the project functionality!

## Usage

### Calculator

```bash
>> brain-calc

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What is the result of the expression?
Question: 4 + 10
Your answer: 14
Correct!
Question: 25 - 11
Your answer: 14
Correct!
Question: 25 * 7
Your answer: 175
Correct!
Congratulations, Sam!
```

### Progression

```bash
>> brain-progression

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What number is missing in the progression?
Question: 5 7 9 11 13 .. 17 19 21 23
Your answer: 15
Correct!
Question: 2 5 8 .. 14 17 20 23 26 29
Your answer: 11
Correct!
Question: 14 19 24 29 34 39 44 49 54 ..
Your answer: 59
Correct!
Congratulations, Sam!
```

### Determining an even number

```bash
>> brain-even

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: no
Correct!
Question: 6
Your answer: yes
Correct!
Question: 7
Your answer: no
Correct!
Congratulations, Sam!
```

### Determining the largest common divisor

```bash
>> brain-gcd

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Find the greatest common divisor of given numbers.
Question: 25 50
Your answer: 25
Correct!
Question: 100 52
Your answer: 4
Correct!
Question: 3 9
Your answer: 3
Correct!
Congratulations, Sam!
```

### Determining a prime number

```bash
>> brain-prime

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 7
Your answer: yes
Correct!
```

## Development

### Useful commands

* `make install` - install all dependencies in the environment.
* `make build` - build the wheel.
* `make lint` - checking code with linter.
* `make test` - run tests.
