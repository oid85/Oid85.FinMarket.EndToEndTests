import config
from datetime import datetime, timedelta
from modules.api_tests import api_list_tickers, api_report, api_diagram_simple, api_diagram_bubble


fromDate = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
toDate = datetime.now().strftime('%Y-%m-%d')

def test_api_futures_watch_list_tickers():
    api_list_tickers(f'{config.api_url}/api/futures/watch-list-tickers')
