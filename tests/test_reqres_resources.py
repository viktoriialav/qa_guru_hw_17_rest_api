import requests
from jsonschema import validate

from reqres_tests.utils.files import load_schema_from_file

url = 'https://reqres.in'
endpoint_list = '/api/unknown'
endpoint_single = '/api/unknown/2'
endpoint_not_found = '/api/unknown/23'

name = "morpheus"
job = "leader"


def test_list_resources():
    response = requests.get(url=url + endpoint_list)

    assert response.status_code == 200
    validate(response.json(), schema=load_schema_from_file('get_list_resources.json'))


def test_single_resource_user():
    response = requests.get(url=url + endpoint_single)

    assert response.status_code == 200
    validate(response.json(), schema=load_schema_from_file('get_single_resource.json'))


def test_single_resource_not_found():
    response = requests.get(url=url + endpoint_not_found)

    assert response.status_code == 404
    validate(response.json(), schema={})
