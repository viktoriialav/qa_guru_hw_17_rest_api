import json

from jsonschema import validate
import requests

from reqres_tests.utils.files import file_path

url = 'https://reqres.in'
endpoint = '/api/login'

email = "eve.holt@reqres.in"
password = "cityslicka"

payload = {
        "email": email,
        "password": password
    }


def test_log_in_user_successeful_status_code():
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url=url + endpoint, headers=headers, json=payload)

    assert response.status_code == 200


def test_log_in_user_unsuccesseful_status_code():
    new_payload = dict(payload)
    new_payload.popitem()

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url=url + endpoint, headers=headers, json=new_payload)

    assert response.status_code == 400


def test_log_in_user_successeful_schema_response():
    response = requests.post(url=url + endpoint, data=payload)

    with open(file_path('post_log_in_successful.json'), encoding='utf-8') as file:
        validate(response.json(), schema=json.load(file))


def test_log_in_user_unsuccesseful_schema_response():
    new_payload = dict(payload)
    new_payload.popitem()

    response = requests.post(url=url + endpoint, data=new_payload)

    with open(file_path('post_log_in_unsuccessful.json'), encoding='utf-8') as file:
        validate(response.json(), schema=json.load(file))
