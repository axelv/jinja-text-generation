import click
import json
import logging
from jinja2 import Environment, PackageLoader, select_autoescape
from jinja_text_generation.filters.table import do_pad_column
from jinja_text_generation.filters.pprint import do_pprint
logging.basicConfig(level=logging.INFO)
env = Environment(
    loader=PackageLoader("jinja_text_generation"),
    autoescape=select_autoescape()
)

# Register the filters to help with text generation
env.filters["pad_column"] = do_pad_column
env.filters["pprint"] = do_pprint

@click.argument("input_file", type=click.File("r"))
@click.option("--type", "-t")
@click.command()
def cli(input_file, type):
    """Generate the narrative for a questionnaire"""
    template = env.get_template(f"{type}.txt")
    # Load the JSON file and render using the template
    print(template.render(table=json.load(input_file)))
