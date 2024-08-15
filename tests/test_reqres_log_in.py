import requests
from jsonschema import validate

from reqres_tests.utils.files import load_schema_from_file

url = 'https://reqres.in'
endpoint = '/api/login'

email = "eve.holt@reqres.in"
password = "cityslicka"

payload = {
    "email": email,
    "password": password
}


def test_log_in_user_successeful_status_code():
    response = requests.post(url=url + endpoint, data=payload)

    assert response.status_code == 200


def test_log_in_user_unsuccesseful_status_code():
    new_payload = dict(payload)
    new_payload.popitem()

    response = requests.post(url=url + endpoint, data=new_payload)

    assert response.status_code == 400


def test_log_in_user_successeful_schema_response():
    response = requests.post(url=url + endpoint, data=payload)

    validate(response.json(), schema=load_schema_from_file('post_log_in_successful.json'))


def test_log_in_user_unsuccesseful_schema_response():
    new_payload = dict(payload)
    new_payload.popitem()

    response = requests.post(url=url + endpoint, data=new_payload)

    validate(response.json(), schema=load_schema_from_file('post_log_in_unsuccessful.json'))
