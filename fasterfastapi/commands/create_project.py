import click
import os
from fasterfastapi.utils.template_generation import create_structure
from fasterfastapi.utils.config import load_config, save_config

@click.command()
@click.argument("project_name")
def create_project(project_name):
   path = os.getcwd()
   if load_config() !=  {}:
      click.echo("Project already created")
      return

   click.echo(f"Creating project at {path}")
   structure = {project_name: {
      "src": {
         "main.py":'main.py.jinja',
         "config.py":'',
         "logging.py": '',
         "rate_limiting.py":'',
      },
      "requirements.txt":'',
      }
   }

   items = {
      "name": project_name,
      "routes": []
   }

   create_structure(path, structure, items)
   save_config(structure)


