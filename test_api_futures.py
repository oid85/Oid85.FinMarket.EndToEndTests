import config
from modules.api_tests import api_list_tickers


def test_api_futures_watch_list_tickers():
    api_list_tickers(f'{config.api_url}/api/futures/watch-list-tickers')
