import json
from pathlib import Path

import tests


def file_path(file_name):
    return str(Path(tests.__file__).parent.parent.joinpath(f'schemas/{file_name}').absolute())


def load_schema_from_file(file_name):
    with open(file_path(file_name), encoding='utf-8') as file:
        schema = json.load(file)
    return schema
