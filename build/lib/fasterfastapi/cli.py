import click

@click.command()
@click.argument("test")
def test(test):
    click.echo(f"Running test: {test}")