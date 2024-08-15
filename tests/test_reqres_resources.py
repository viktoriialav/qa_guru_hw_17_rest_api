import requests
from jsonschema import validate

from reqres_tests.utils.files import load_schema_from_file

url = 'https://reqres.in'
endpoint_list = '/api/unknown'
endpoint_single = '/api/unknown/2'
endpoint_not_found = '/api/unknown/23'

name = "morpheus"
job = "leader"


def test_list_resources_status_code():
    response = requests.get(url=url + endpoint_list)

    assert response.status_code == 200


def test_single_resource_user_status_code():
    response = requests.get(url=url + endpoint_single)

    assert response.status_code == 200


def test_single_resource_not_found_status_code():
    response = requests.get(url=url + endpoint_not_found)

    assert response.status_code == 404


def test_list_resources_schema():
    response = requests.get(url=url + endpoint_list)

    validate(response.json(), schema=load_schema_from_file('get_list_resources.json'))


def test_single_resource_schema():
    response = requests.get(url=url + endpoint_single)

    validate(response.json(), schema=load_schema_from_file('get_single_resource.json'))


def test_single_resource_not_found_schema():
    response = requests.get(url=url + endpoint_not_found)

    validate(response.json(), schema={})
