import json

import requests
from jsonschema import validate

from reqres_tests.utils.files import file_path

url = 'https://reqres.in'
endpoint = '/api/register'

email = "eve.holt@reqres.in"
password = "pistol"

payload = {
    "email": email,
    "password": password
}


def test_register_user_successeful_status_code():
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url=url + endpoint, headers=headers, json=payload)

    assert response.status_code == 200


def test_register_user_unsuccesseful_status_code():
    new_payload = dict(payload)
    new_payload.popitem()

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url=url + endpoint, headers=headers, json=new_payload)

    assert response.status_code == 400


def test_register_user_successeful_schema_response():
    response = requests.post(url=url + endpoint, data=payload)

    with open(file_path('post_register_successful.json'), encoding='utf-8') as file:
        validate(response.json(), schema=json.load(file))


def test_register_user_unsuccesseful_schema_response():
    new_payload = dict(payload)
    new_payload.popitem()

    response = requests.post(url=url + endpoint, data=new_payload)

    with open(file_path('post_register_unsuccessful.json'), encoding='utf-8') as file:
        validate(response.json(), schema=json.load(file))
