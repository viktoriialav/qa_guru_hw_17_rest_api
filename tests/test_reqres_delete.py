import requests

url = 'https://reqres.in'
endpoint = '/api/users/2'


def test_delete_status_code():
    response = requests.delete(url=url + endpoint)

    assert response.status_code == 204
    assert response.text == ''
