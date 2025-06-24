import click
from fasterfastapi.commands.create_project import create_project
from fasterfastapi.commands.create_endpoint import create_endpoint
from fasterfastapi.commands.create_database import add_database
from fasterfastapi.commands.add_jwt_token import add_jwt

@click.group()
def cli():
    pass


cli.add_command(create_project)
cli.add_command(create_endpoint)
cli.add_command(add_database)
cli.add_command(add_jwt)
