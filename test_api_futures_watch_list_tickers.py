import config
from modules.api_list_tickers import api_list_tickers


def test_api_futures_watch_list_tickers():
    url = f'{config.api_url}/api/futures/watch-list-tickers'
    api_list_tickers(url)
