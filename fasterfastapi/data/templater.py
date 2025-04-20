from jinja2 import Environment, FileSystemLoader, Template
import os

def get_environment():
    template_dir = os.path.join(os.path.dirname(__file__), "../templates")
    return Environment(loader=FileSystemLoader(template_dir))


def get_template(template) -> Template:
    env = get_environment()
    return env.get_template(template)