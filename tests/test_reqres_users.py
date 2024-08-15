import json

import requests
from jsonschema import validate

from reqres_tests.utils.files import file_path

url = 'https://reqres.in'
endpoint_list = '/api/users'
endpoint_single = '/api/users/2'
endpoint_not_found = '/api/users/23'

name = "morpheus"
job = "leader"

payload = {
    "name": name,
    "job": job
}


def test_list_users_status_code():
    response = requests.get(url=url + endpoint_list, params={'page': 2})

    assert response.status_code == 200


def test_single_user_status_code():
    response = requests.get(url=url + endpoint_single)

    assert response.status_code == 200


def test_single_user_not_found_status_code():
    response = requests.get(url=url + endpoint_not_found)

    assert response.status_code == 404


def test_list_users_schema():
    response = requests.get(url=url + endpoint_list, params={'page': 2})

    with open(file_path('get_list_users.json'), encoding='utf-8') as file:
        validate(response.json(), json.load(file))


def test_single_user_schema():
    response = requests.get(url=url + endpoint_single)

    with open(file_path('get_single_user.json'), encoding='utf-8') as file:
        validate(response.json(), json.load(file))


def test_single_user_not_found_schema():
    response = requests.get(url=url + endpoint_not_found)

    validate(response.json(), schema={})
