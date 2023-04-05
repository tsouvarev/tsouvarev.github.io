import json
import os

from pathlib import Path

import jinja2
import typer

environment = jinja2.Environment()


def generate(page_name: str, objects_file: Path):
    with open(objects_file) as f:
        objects = json.load(f)

    with open('template.html') as f:
        template = environment.from_string(f.read())

    if not os.path.exists(page_name):
        os.mkdir(page_name)

    with open(f'{page_name}/index.html', 'w') as f:
        rendered = template.render(page=page_name.capitalize(), objects=objects)
        f.write(rendered)


if __name__ == "__main__":
    typer.run(generate)