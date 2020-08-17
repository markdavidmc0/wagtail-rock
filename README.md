# Wagtail Rock Site

First CMS project for Wagtail Rock Studio.

## Creating a virtual environment
Before installing project requirements, it is advised to create a virtual environment:
1. Ensure that you are in the project root directory.
2. Execute `python3 -m venv env` to create a virtual environment in the present working directory.
3. Execute `source env/bin/activate` to activate the virtual environment.

## Installing requirements
After activating your virtual environment, run: </br>
`pip3 install -r requirements.txt`

## Code formatting and linting
Ensure that commit hooks are installed using the following:
`pre-commit install`

Before committing any code, run the following to detect formatting errors on staged changes: </br>
`pre-commit run`

If you want to run auto PEP8 and linting on all files, not just changed files, run: </br>
`pre-commit run --all-files`

