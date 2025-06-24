import os

import click

from fasterfastapi.utils.config import load_config
from fasterfastapi.utils.template_generation import create_structure, add_to_config 


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
        "database.py": "mysqldatabase.py.jinja",
        "config.py": "config.py.jinja",
    }
    content = {"MYSQL_DATABASE_URI:": uri, "MYSQL_DATABASE_NAME": project_name} 
    
    create_structure(path, structure, {})
    add_to_config(path + "/config.py", content, "Config") 
