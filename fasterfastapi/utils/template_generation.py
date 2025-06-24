import ast
import os

import click
from jinja2 import Environment, FileSystemLoader, Template
from redbaron import RedBaron


def get_environment():
    template_dir = os.path.join(os.path.dirname(__file__), "../templates")
    return Environment(loader=FileSystemLoader(template_dir))


def get_template(template) -> Template:
    env = get_environment()
    return env.get_template(template)


def create_structure(parent_path, structure, items: dict):
    for name, value in structure.items():
        if isinstance(value, dict):
            os.makedirs(f"{parent_path}/{name}", exist_ok=True)
            create_structure(parent_path + "/" + name, value, items)

        if isinstance(value, str):
            with open(parent_path + "/" + name, "w") as f:
                if value == "":
                    f.write(value)
                    continue
                rendered = get_template(value).render(items=items)
                f.write(rendered)


def add_to_config(file_path: str, content: dict[str, str], class_name: str):
    try:
        red = RedBaron(open(file_path).read())
    except FileNotFoundError:
        click.echo(f"Creating new config file")
        create_structure(
            os.path.dirname(file_path), {"config.py": "config.py.jinja"}, {}
        )
        red = RedBaron(open(file_path).read())
    config_class = red.find("class", name=class_name)

    # Have to remove all passes because there is a pass in the template
    # that we need to have there otherwise redbaron will throw an error
    for node in config_class.find_all("pass"):
        config_class.remove(node)

    for key, value in content.items():
        # Here to make sure that we do not add the same key twice
        if not config_class.find("AssignmentNode", target=lambda t: t.value == key):
            config_class.append(f"{key} = {value}")
    with open(file_path, "w") as f:
        f.write(red.dumps())
