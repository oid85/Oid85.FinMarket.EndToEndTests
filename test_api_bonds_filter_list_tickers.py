import config
from modules.api_list_tickers import api_list_tickers


def test_api_bonds_filter_list_tickers():
    url = f'{config.api_url}/api/bonds/filter-list-tickers'
    api_list_tickers(url)
