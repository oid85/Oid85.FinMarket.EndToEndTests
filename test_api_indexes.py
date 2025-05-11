import config
from datetime import datetime, timedelta
from modules.api_tests import api_list_tickers, api_report, api_diagram_simple, api_diagram_bubble


fromDate = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
toDate = datetime.now().strftime('%Y-%m-%d')

def test_api_indexes_watch_list_tickers():
    api_list_tickers(f'{config.api_url}/api/indexes/watch-list-tickers')


def test_api_indexes_report_aggregated_analyse():
    api_report(f'{config.api_url}/api/indexes/report/aggregated-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'indexes/watchlist' })


def test_api_indexes_report_supertrend_analyse():
    api_report(f'{config.api_url}/api/indexes/report/supertrend-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'indexes/watchlist' })


def test_api_indexes_report_candle_sequence_analyse():
    api_report(f'{config.api_url}/api/indexes/report/candle-sequence-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'indexes/watchlist' })


def test_api_indexes_report_rsi_analyse():
    api_report(f'{config.api_url}/api/indexes/report/rsi-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'indexes/watchlist' })


def test_api_indexes_report_atr_analyse():
    api_report(f'{config.api_url}/api/indexes/report/atr-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'indexes/watchlist' })


def test_api_indexes_report_donchian_analyse():
    api_report(f'{config.api_url}/api/indexes/report/donchian-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'indexes/watchlist' })


def test_api_indexes_report_yield_ltm_analyse():
    api_report(f'{config.api_url}/api/indexes/report/yield-ltm-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'indexes/watchlist' })


def test_api_indexes_report_drawdown_from_maximum_analyse():
    api_report(f'{config.api_url}/api/indexes/report/drawdown-from-maximum-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'indexes/watchlist' })


def test_api_indexes_report_active_market_events_analyse():
    api_report(f'{config.api_url}/api/indexes/report/active-market-events-analyse',
        { "tickerList": 'indexes/watchlist' })


def test_api_indexes_diagram_daily_close_prices():
    api_diagram_simple(f'{config.api_url}/api/indexes/diagram/daily-close-prices',
        { "from": fromDate, "to": toDate, "tickerList": 'indexes/watchlist' })
