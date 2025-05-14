import click

from build.lib.fasterfastapi.commands.create_project import create_structure
from fasterfastapi.utils.config import load_config, save_config
import os

@click.command()
def add_database():

    db_name = click.prompt("What is the name of the database: ")
    db_host = click.prompt("What is the database host: ")
    db_port = click.prompt("What is the port of the database: ")
    db_user = click.prompt("What is the user name of the database: ")
    db_pass = click.prompt("What is the password of the database: ")

    config = load_config()
    if config == {}:
        click.echo("Project does not exist yet.")

    project_name = next(iter(config))

    uri = f"mysql+asyncmy://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    path = f"{os.getcwd()}/{project_name}/src"

    structure = {
        'database.py':'mysqldatabase.py.jinja',
        'config.py':'config.py.jinja',
    }

    items = {"uri": uri, "db_name":db_name,}

    create_structure(path, structure, items)





