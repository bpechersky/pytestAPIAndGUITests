import requests

def test_delete_user():
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "reqres-free-v1"
    }
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)
    assert response.status_code == 204