import requests

def test_create_user():
    payload = {"name": "morpheus", "job": "leader"}
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "morpheus"