from pathlib import Path

import tests


def file_path(file_name):
    return str(Path(tests.__file__).parent.parent.joinpath(f'schemas/{file_name}').absolute())