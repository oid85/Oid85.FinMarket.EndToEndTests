import config
from datetime import datetime, timedelta
from modules.api_tests import api_list_tickers, api_report, api_diagram_simple, api_diagram_bubble


fromDate = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
toDate = datetime.now().strftime('%Y-%m-%d')

def test_api_futures_watch_list_tickers():
    api_list_tickers(f'{config.api_url}/api/futures/watch-list-tickers')


def test_api_futures_report_aggregated_analyse():
    api_report(f'{config.api_url}/api/futures/report/aggregated-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'futures/watchlist' })


def test_api_futures_report_supertrend_analyse():
    api_report(f'{config.api_url}/api/futures/report/supertrend-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'futures/watchlist' })


def test_api_futures_report_candle_sequence_analyse():
    api_report(f'{config.api_url}/api/futures/report/candle-sequence-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'futures/watchlist' })


def test_api_futures_report_candle_volume_analyse():
    api_report(f'{config.api_url}/api/futures/report/candle-volume-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'futures/watchlist' })


def test_api_futures_report_rsi_analyse():
    api_report(f'{config.api_url}/api/futures/report/rsi-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'futures/watchlist' })


def test_api_futures_report_atr_analyse():
    api_report(f'{config.api_url}/api/futures/report/atr-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'futures/watchlist' })


def test_api_futures_report_donchian_analyse():
    api_report(f'{config.api_url}/api/futures/report/donchian-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'futures/watchlist' })


def test_api_futures_report_yield_ltm_analyse():
    api_report(f'{config.api_url}/api/futures/report/yield-ltm-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'futures/watchlist' })


def test_api_futures_report_spread_analyse():
    api_report(f'{config.api_url}/api/futures/report/spread-analyse',
        { "tickerList": 'futures/watchlist' })


def test_api_futures_report_active_market_events_analyse():
    api_report(f'{config.api_url}/api/futures/report/active-market-events-analyse',
        { "tickerList": 'futures/watchlist' })


def test_api_futures_diagram_daily_close_prices():
    api_diagram_simple(f'{config.api_url}/api/futures/diagram/daily-close-prices',
        { "from": fromDate, "to": toDate, "tickerList": 'futures/watchlist' })
