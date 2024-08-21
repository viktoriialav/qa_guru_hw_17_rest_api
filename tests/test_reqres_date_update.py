import requests
from jsonschema import validate

from reqres_tests.utils.files import load_schema_from_file

url = 'https://reqres.in'
endpoint = '/api/users/2'

name = "morpheus"
job = "zion resident"

payload = {
    "name": name,
    "job": job
}


def test_date_update():
    response = requests.put(url=url + endpoint, data=payload)

    assert response.status_code == 200
    validate(response.json(), schema=load_schema_from_file('put_date_update.json'))
