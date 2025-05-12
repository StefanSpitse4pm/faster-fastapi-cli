import sys

import click
import os
import json
from pathlib import Path
from fasterfastapi.utils.structure import does_project_data_exist
from fasterfastapi.utils.template_generation import get_template
from appdirs import user_data_dir


@click.command()
@click.argument("project_name")
@click.pass_context
def create_project(ctx, project_name):
   state = ctx.obj

   if does_project_data_exist(project_name):
      click.echo("Project already exists")
      return

   path = os.getcwd()


   click.echo(f"Creating project at {path}")
   data_dir = user_data_dir(project_name)
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
   os.makedirs(data_dir, exist_ok=True)
   root_dir = os.path.join(data_dir, "structure.json")
   with open(root_dir, "w") as file:
      json.dump(structure, file)
   state.created_project = True

def create_structure(parent_path, structure, items):
   for name, value in structure.items():
      if isinstance(value, dict):
         os.mkdir(f"{parent_path}/{name}")
         create_structure(parent_path + "/" + name, value, items)

      if isinstance(value, str):
         with open(parent_path + "/" + name, 'w') as f:
            if value == "":
               f.write(value)
               continue
            rendered = get_template(value).render(items=items)
            f.write(rendered)


