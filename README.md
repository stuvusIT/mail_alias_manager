# mail_alias_manager

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![GitHub license](https://img.shields.io/github/license/stuvusIT/mail_alias_manager)](https://github.com/stuvusIT/mail_alias_manager/blob/main/LICENSE)
![Python: >= 3.7](https://img.shields.io/badge/python-^3.7-blue)

A small flask app for mananing mail aliases in a postgres database.
## Development

This package uses Poetry ([documentation](https://python-poetry.org/docs/)).

Run `poetry install` to install dependencies.

Add `.env` file with the following content into the repository root.

```bash
FLASK_APP=mail_alias_manager # rename this if you rename the package!
FLASK_ENV=development # set to production of in production!
```

Run the development server with

```bash
poetry run flask run
```
### VSCode

For vscode install the python extension and add the poetry venv path to the folders the python extension searches vor venvs.

On linux:

```json
{
    "python.venvFolders": [
        "~/.cache/pypoetry/virtualenvs"
    ]
}
```
### Babel

```bash
# initial
poetry run pybabel extract -F babel.cfg -o messages.pot .
# create language
poetry run pybabel init -i messages.pot -d translations -l en
# compile translations to be used
poetry run pybabel compile -d translations
# extract updated strings
poetry run pybabel update -i messages.pot -d translations
```

### SQLAlchemy

```bash
# create dev db (this will NOT run migrations!)
poetry run flask create-db
# drop dev db
poetry run flask drop-db
```

### Migrations

```bash
# create a new migration after changes in the db
poetry run flask db migrate -m "Initial migration."
# upgrade db to the newest migration
poetry run flask db upgrade
# help
poetry run flask db --help
```
