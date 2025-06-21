import os

import click
from fasterfastapi.utils.config import load_config, save_config
from fasterfastapi.utils.template_generation import create_structure
@click.command()
@click.argument("endpoint_name")
@click.option('--get', is_flag=True, help="Adds a template of a get endpoint")
@click.option('--post', is_flag=True, help="Adds a template of a post endpoint")
@click.option('--delete', is_flag=True, help="Adds a template of a delete endpoint")
@click.option('--put', is_flag=True, help="Adds a template of a put endpoint")
@click.option("--crud", is_flag=True, help="Adds all of the crud enpoints")
def create_endpoint(endpoint_name, get, post, delete, put, crud):
    if crud:
        get = post = delete = put = True

    config = load_config()
    if config == {}:
       click.echo("Project does not exist yet.")

    project_name = next(iter(config))

    path = f"{os.getcwd()}/{project_name}/src/{endpoint_name}"
    structure = {endpoint_name: {
        'router.py':'router.py.jinja',
        'models.py':'',
        'dependecies.py':'',
        'service.py':'',

    }}
    items = {"name":endpoint_name, "_get": get, "post": post, "delete": delete, "put": put}
    config.update(structure)

    with open(f"{project_name}/src/main.py", "r+") as file:
        original = file.read()
        file.seek(0)
        file.write(f"from .{endpoint_name}.router import router as {endpoint_name}_route\n{original}")

    with open(f"{project_name}/src/main.py", "a") as file:
        file.write(f"app.include_router({endpoint_name}_route)\n  ")

    try:
        os.mkdir(path)
    except FileExistsError:
        click.echo(f"endpoint {endpoint_name}_ already exists!")
        return

    create_structure(path, structure[endpoint_name], items)
    save_config(config)
