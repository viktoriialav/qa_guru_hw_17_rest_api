import requests
from jsonschema import validate

from reqres_tests.utils.files import load_schema_from_file

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


def test_list_users():
    response = requests.get(url=url + endpoint_list)

    assert response.status_code == 200
    validate(response.json(), schema=load_schema_from_file('get_list_users.json'))


def test_single_user():
    response = requests.get(url=url + endpoint_single)

    assert response.status_code == 200
    validate(response.json(), schema=load_schema_from_file('get_single_user.json'))


def test_single_user_not_found():
    response = requests.get(url=url + endpoint_not_found)

    assert response.status_code == 404
    validate(response.json(), schema={})


def test_number_of_users_on_last_page_with_special_per_page():
    page = 3
    per_page = 5
    response = requests.get(url=url + endpoint_list, params={'page': page, 'per_page': per_page})

    assert len(response.json()['data']) + (page * per_page - response.json()['total']) == per_page


def test_request_returns_unique_users():
    page = 1

    response_1 = requests.get(url=url + endpoint_list)
    per_page = response_1.json()['total']
    response_2 = requests.get(url=url + endpoint_list, params={'page': page, 'per_page': per_page})

    ids = [elem['id'] for elem in response_2.json()['data']]

    assert len(ids) == len(set(ids))


def test_page_in_request_the_same_as_page_in_response():
    page = 2
    response = requests.get(url=url + endpoint_list, params={'page': page})

    assert response.json()['page'] == page
