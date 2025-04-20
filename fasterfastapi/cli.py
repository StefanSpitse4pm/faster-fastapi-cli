import click
from fasterfastapi.commands.create_project import create_project

@click.group()
def cli():
    pass

cli.add_command(create_project)