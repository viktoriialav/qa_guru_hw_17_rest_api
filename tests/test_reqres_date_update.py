import json

import requests
from jsonschema import validate

from reqres_tests.utils.files import file_path

url = 'https://reqres.in'
endpoint = '/api/users/2'

name = "morpheus"
job = "zion resident"

payload = {
    "name": name,
    "job": job
}


def test_date_update_status_code():
    response = requests.put(url=url + endpoint, data=payload)

    assert response.status_code == 200


def test_date_update_schema():
    response = requests.put(url=url + endpoint, data=payload)

    with open(file_path('put_date_update.json'), encoding='utf-8') as file:
        validate(response.json(), schema=json.load(file))
