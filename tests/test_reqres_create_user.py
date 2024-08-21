import requests
from jsonschema import validate

from reqres_tests.utils.files import load_schema_from_file

url = 'https://reqres.in'
endpoint = '/api/users'

name = "morpheus"
job = "leader"

payload = {
    "name": name,
    "job": job
}


def test_create_user():
    response = requests.post(url=url + endpoint, data=payload)

    assert response.status_code == 201
    validate(response.json(), schema=load_schema_from_file('post_create_user.json'))


def test_create_user_right_data_in_response():
    response = requests.post(url=url + endpoint, data=payload)

    data = response.json()
    assert data['name'] == name
    assert data['job'] == job
