import os

import click

from fasterfastapi.utils.config import load_config, save_config
from fasterfastapi.utils.template_generation import create_structure


@click.command()
@click.argument("project_name")
def create_project(project_name):
    path = os.getcwd()
    try:
        if load_config()[project_name]:
            click.echo("Project already created")
            return
    except KeyError:
        pass

    click.echo(f"Creating project at {path}")
    structure = {
        project_name: {
            "src": {
                "main.py": "main.py.jinja",
                "logger.py": "logger.py.jinja",
                "middleware.py": "middleware.py.jinja",
            },
            "requirements.txt": "requirements.txt.jinja",
        }
    }

    items = {"name": project_name, "routes": []}

    create_structure(path, structure, items)
    save_config(structure)
