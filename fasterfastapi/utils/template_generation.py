from jinja2 import Environment, FileSystemLoader

def setup_env(template_dir='templates'):
    return Environment(loader=FileSystemLoader(template_dir))

def render_template(template, context=None):
    if context is None:
        context = {}

    env = setup_env()
    template = env.get_template(template)
    rendered = template.render(context)
    return rendered