import click
import os
from fasterfastapi.commands import create_endpoint
from fasterfastapi.utils.config import load_config
from fasterfastapi.utils.template_generation import add_to_config 

@click.command()
def add_jwt():

    config = load_config()
    if config == {}:
        click.echo("Project does not exist yet.")

    secret_key = click.prompt("What is the secret key for JWT: ")
    algorithm = click.prompt(
        "What is the algorithm for JWT (default: HS256): ", default="HS256"
    )
    access_token_expire_minutes = click.prompt(
        "What is the access token expire time in minutes (default: 30): ",
        default=30,
        type=int,
    )
    login = click.prompt(
        "Do you want to add a login endpoint? (yes/no): ",
        default="yes",
        type=click.Choice(["yes", "no"], case_sensitive=False),
    )
    jwt_config = {
        "secret_key": f"'{secret_key}'",
        "algorithm": f"'{algorithm}'",
        "access_token_expire_minutes": access_token_expire_minutes,
        "login_endpoint": login.lower() == "yes",
    }
    if jwt_config["login_endpoint"]:
        ctx = click.get_current_context()
        ctx.invoke(
            create_endpoint.create_endpoint,
            post=True,
            get=True,
            endpoint_name="auth",
            custom_endpoint="Auth",
        )

    project_name = next(iter(config))
    path = f"{os.getcwd()}/{project_name}/src/config.py"
    add_to_config(path, dict(list(jwt_config.items())[:-1]), "Config")
