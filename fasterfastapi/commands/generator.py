import click
import os

@click.command()
@click.argument("project_name")
def create_project(project_name):
   path = os.getcwd()
   click.echo(f"Creating project at {path}")

   structure = {project_name: {
      "src": {"main.py":''}

   }}
   create_structure(path, structure)

def create_structure(parent_path, structure):
   for name, value in structure.items():
      print(f"{name} -> {value}")

      if isinstance(value, dict):
         os.mkdir(f"{parent_path}/{name}")
         create_structure(parent_path + "/" + name, value)

      if isinstance(value, str):
         with open(parent_path + "/" + name, 'w') as f:
            f.write(name)
