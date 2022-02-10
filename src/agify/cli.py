import click
from .client import AgifyAPIClient

@click.command()
@click.argument("name")
def run(name):
    name_data = AgifyAPIClient.fetch(name=name)
    print(name_data)