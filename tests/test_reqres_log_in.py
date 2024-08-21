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


def test_log_in_user_successful():
    response = requests.post(url=url + endpoint, data=payload)

    assert response.status_code == 200
    validate(response.json(), schema=load_schema_from_file('post_log_in_successful.json'))


def test_log_in_user_unsuccessful():
    new_payload = dict(payload)
    new_payload.popitem()

    response = requests.post(url=url + endpoint, data=new_payload)

    assert response.status_code == 400
    validate(response.json(), schema=load_schema_from_file('post_log_in_unsuccessful.json'))
