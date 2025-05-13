import click
from fasterfastapi.commands.create_project import create_project
from fasterfastapi.commands.create_endpoint import create_endpoint

@click.group()
def cli():
    pass
cli.add_command(create_project)
cli.add_command(create_endpoint)
