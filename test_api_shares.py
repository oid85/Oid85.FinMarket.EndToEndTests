import config
from modules.api_tests import api_list_tickers, api_report


def test_api_shares_watch_list_tickers():
    api_list_tickers(f'{config.api_url}/api/shares/watch-list-tickers')


def test_api_shares_report_aggregated_analyse():
    api_report(f'{config.api_url}/api/shares/report/aggregated-analyse', 'shares/watchlist')
