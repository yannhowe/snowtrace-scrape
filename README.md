# snowtrace-scrape
Scrapes transaction data in JSON format from snowtrace API.

## Quickstart
```
# Install pipenv - https://pipenv.pypa.io/en/latest/#install-pipenv-today
pip install --user pipenv

# Insert Snowtrace API key into .env file
nano .env

pipenv install
pipenv run python scrape.py
```