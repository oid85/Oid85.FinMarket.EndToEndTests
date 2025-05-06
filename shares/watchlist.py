import requests


class TestGetWatchList:
    def test_watchlist(self):
        body = {"username": "test@test.com", "password": "Password"}
        response = requests.post("https://stores-tests-api.herokuapp.com/register", json=body)
        assert response.status_code == 201
        assert response.json().get('message') == 'User created successfully.'
        assert response.json().get('uuid')
        assert isinstance(response.json().get('uuid'), int)
        print(response.text)