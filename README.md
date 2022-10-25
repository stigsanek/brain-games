# Brain games

[![Github Actions Status](https://github.com/stigsanek/python-project-49/workflows/python-ci/badge.svg)](https://github.com/stigsanek/python-project-49/actions)
[![Actions Status](https://github.com/stigsanek/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/stigsanek/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/fcb2587dfb95cbc6f1e7/maintainability)](https://codeclimate.com/github/stigsanek/python-project-49/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/fcb2587dfb95cbc6f1e7/test_coverage)](https://codeclimate.com/github/stigsanek/python-project-49/test_coverage)

"Brain games" is a set of five console games based on the popular mobile brain-pumping apps. Each game asks questions
that need to be answered correctly. After three correct answers, the game is considered completed. Incorrect answers end
the game and prompt you to play it again. Games:

* Calculator. Arithmetic expressions to be calculated.
* Progression. Finding missing numbers in a sequence of numbers.
* Determining an even number.
* Determining the largest common divisor.
* Determining a prime number.

## Install

1. Install [poetry](https://python-poetry.org/).
2. Run `make install` or `poetry install` in the project directory.

## Usage

### From project

Commands for launching games:

- Calculator: `make brain-calc` or `poetry run brain-calc`
- Progression: `make brain-progression` or `poetry run brain-progression`
- Determining an even number: `make brain-even` or `poetry run brain-even`
- Determining the largest common divisor: `make brain-gcd` or `poetry run brain-gcd`
- Determining a prime number: `make brain-prime` or `poetry run brain-prime`

### Wheel

You can build the wheel for later installation in a separate virtual environment with command `make build`
or `poetry build`.
After installing the package in the virtual environment, the games can be launched using the commands:

- Calculator: `brain-calc`
- Progression: `brain-progression`
- Determining an even number: `brain-even`
- Determining the largest common divisor: `brain-gcd`
- Determining a prime number: `brain-prime`

## Example

### Calculator

```
brain-calc

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

```
brain-progression

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

```
brain-even

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

```
brain-gcd

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

```
brain-prime

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 7
Your answer: yes
Correct!
```
