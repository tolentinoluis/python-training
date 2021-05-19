# python-training

# Prerequisites

## Python

You will need to have [Python](https://www.python.org/) installed (used v3.9.5) and have [Pipenv](https://pypi.org/project/pipenv/) installed to manage python packages and creating a virtual environment. Run the commands shown here from bash or shell.

## Pipenv

To install pipenv:
```bash
pip install pipenv
```

## Webdriver

The UI tests requires the use of a web driver [chromedriver](https://chromedriver.chromium.org/) to run the UI tests. Make sure the chromdriver executable is added to `PATH`

# Setup
Open the project from shell and create your virtual environment from the [Pipfile](Pipfile) on the main project folder. Run command
```bash
py -3.7 -m pipenv install
```
## Run test

For running the ui tests, use:
```bash
pipenv run python -m pytest -s
```
