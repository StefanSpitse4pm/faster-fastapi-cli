from jinja2 import Environment, FileSystemLoader, Template
import os

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
         with open(parent_path + "/" + name, 'w') as f:
            if value == "":
               f.write(value)
               continue
            rendered = get_template(value).render(items=items)
            f.write(rendered)
