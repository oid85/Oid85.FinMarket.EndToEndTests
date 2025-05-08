import requests
import config


def test_api_currencies_watch_list_tickers():
    # arrange
    url = f'{config.api_url}/api/currencies/watch-list-tickers'

    # act
    response = requests.get(url)
    response_json = response.json()
    result = response_json["result"]

    # assert
    assert response.status_code == 200
    assert len(result) > 0