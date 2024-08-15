import requests
from jsonschema import validate

from reqres_tests.utils.files import load_schema_from_file

url = 'https://reqres.in'
endpoint = '/api/register'

email = "eve.holt@reqres.in"
password = "pistol"

payload = {
    "email": email,
    "password": password
}


def test_register_user_successful_status_code():
    response = requests.post(url=url + endpoint, json=payload)

    assert response.status_code == 200


def test_register_user_unsuccessful_status_code():
    new_payload = dict(payload)
    new_payload.popitem()

    response = requests.post(url=url + endpoint, json=new_payload)

    assert response.status_code == 400


def test_register_user_successful_schema_response():
    response = requests.post(url=url + endpoint, data=payload)

    validate(response.json(), schema=load_schema_from_file('post_register_successful.json'))


def test_register_user_unsuccessful_schema_response():
    new_payload = dict(payload)
    new_payload.popitem()

    response = requests.post(url=url + endpoint, data=new_payload)

    validate(response.json(), schema=load_schema_from_file('post_register_unsuccessful.json'))
