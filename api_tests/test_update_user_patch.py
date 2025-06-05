import requests

def test_update_user_patch():
    payload = {"job": "zion resident"}
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "reqres-free-v1"
    }
    response = requests.put("https://reqres.in/api/users/2", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["job"] == "zion resident"