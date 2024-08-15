import json

import requests
from jsonschema import validate

from reqres_tests.utils.files import file_path

url = 'https://reqres.in'
endpoint = '/api/users'

name = "morpheus"
job = "leader"

payload = {
    "name": name,
    "job": job
}


def test_create_user_status_code():
    response = requests.post(url=url + endpoint, data=payload)

    assert response.status_code == 201


def test_create_user_schema():
    response = requests.post(url=url + endpoint, data=payload)

    with open(file_path('post_create_user.json'), encoding='utf-8') as file:
        validate(response.json(), schema=json.load(file))
