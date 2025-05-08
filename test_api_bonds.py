import config
from modules.api_tests import api_list_tickers


def test_api_bonds_filter_list_tickers():
    api_list_tickers(f'{config.api_url}/api/bonds/filter-list-tickers')

def test_api_bonds_watch_list_tickers():
    api_list_tickers(f'{config.api_url}/api/bonds/watch-list-tickers')