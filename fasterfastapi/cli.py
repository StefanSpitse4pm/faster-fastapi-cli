import click
from fasterfastapi.commands.generator import create_project

@click.group()
def cli():
    pass

cli.add_command(create_project)