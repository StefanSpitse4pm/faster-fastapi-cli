import click
from fasterfastapi.commands.create_project import create_project
from fasterfastapi.state import AppState
@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(AppState)

cli.add_command(create_project)