# Brain games

[![Actions Status](https://github.com/stigsanek/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/stigsanek/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/fcb2587dfb95cbc6f1e7/maintainability)](https://codeclimate.com/github/stigsanek/python-project-49/maintainability)

The project contains 5 console games:

- `brain-calc` - calculator
- `brain-even` - parity check
- `brain-gcd`- greatest common divisor
- `brain-prime` - is it a prime number?
- `brain-progression` - arithmetic progression

## Install

1. Install [poetry](https://python-poetry.org/).
2. Run `make install` or `poetry install` in the project directory.

## Usage

### From project

Commands for launching games:

- `make brain-even` or `poetry run brain-even`
- `make brain-calc` or `poetry run brain-calc`
- `make brain-gcd` or `poetry run brain-gcd`
- `make brain-progression` or `poetry run brain-progression`
- `make brain-prime` or `poetry run brain-prime`

### Wheel

You can build the wheel for later installation in a separate virtual environment with command `make build`
or `poetry build`.
After installing the package in the virtual environment, the games can be launched using the commands:

- `brain-calc`
- `brain-even`
- `brain-gcd`
- `brain-prime`
- `brain-progression`
