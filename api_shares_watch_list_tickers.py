import requests
import config


def test_watchlist(self):
    response = requests.get(f'{config.api_url}/api/shares/watch-list-tickers')
    assert response.status_code == 200
