import config
from modules.api_tests import api_list_tickers


def test_api_currencies_watch_list_tickers():
    api_list_tickers(f'{config.api_url}/api/currencies/watch-list-tickers')
