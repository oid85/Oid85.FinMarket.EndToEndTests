import config
from modules.api_list_tickers import api_list_tickers


def test_api_shares_watch_list_tickers():
    url = f'{config.api_url}/api/shares/watch-list-tickers'
    api_list_tickers(url)
