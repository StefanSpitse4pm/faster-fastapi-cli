import click
import os
import json
from pathlib import Path
from fasterfastapi import utils
from fasterfastapi.utils.template_generation import get_

@click.command()
@click.argument("project_name")
def create_project(project_name):
   path = os.getcwd()
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
   root_dir = Path(__file__).parent
   print(root_dir)
   with open(f"{root_dir}/structure.json", "w") as file:
      json.dump(structure, file)

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


