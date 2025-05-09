import config
from datetime import datetime, timedelta
from modules.api_tests import api_list_tickers, api_report, api_diagram_simple, api_diagram_bubble


fromDate = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
toDate = datetime.now().strftime('%Y-%m-%d')

fromDateTime = (datetime.now() - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
toDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def test_api_shares_watch_list_tickers():
    api_list_tickers(f'{config.api_url}/api/shares/watch-list-tickers')


def test_api_shares_report_aggregated_analyse():
    api_report(f'{config.api_url}/api/shares/report/aggregated-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'shares/watchlist' })


def test_api_shares_report_supertrend_analyse():
    api_report(f'{config.api_url}/api/shares/report/supertrend-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'shares/watchlist' })


def test_api_shares_report_candle_sequence_analyse():
    api_report(f'{config.api_url}/api/shares/report/candle-sequence-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'shares/watchlist' })


def test_api_shares_report_candle_volume_analyse():
    api_report(f'{config.api_url}/api/shares/report/candle-volume-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'shares/watchlist' })


def test_api_shares_report_rsi_analyse():
    api_report(f'{config.api_url}/api/shares/report/rsi-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'shares/watchlist' })


def test_api_shares_report_atr_analyse():
    api_report(f'{config.api_url}/api/shares/report/atr-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'shares/watchlist' })


def test_api_shares_report_donchian_analyse():
    api_report(f'{config.api_url}/api/shares/report/donchian-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'shares/watchlist' })


def test_api_shares_report_yield_ltm_analyse():
    api_report(f'{config.api_url}/api/shares/report/yield-ltm-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'shares/watchlist' })


def test_api_shares_report_drawdown_from_maximum_analyse():
    api_report(f'{config.api_url}/api/shares/report/drawdown-from-maximum-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'shares/watchlist' })


def test_api_shares_report_dividend_analyse():
    api_report(f'{config.api_url}/api/shares/report/dividend-analyse',
        { "tickerList": 'shares/watchlist' })


def test_api_shares_report_multiplicator_analyse():
    api_report(f'{config.api_url}/api/shares/report/multiplicator-analyse',
        { "tickerList": 'shares/watchlist' })


def test_api_shares_report_forecast_target_analyse():
    api_report(f'{config.api_url}/api/shares/report/forecast-target-analyse',
        { "tickerList": 'shares/watchlist' })


def test_api_shares_report_forecast_consensus_analyse():
    api_report(f'{config.api_url}/api/shares/report/forecast-consensus-analyse',
        { "tickerList": 'shares/watchlist' })


def test_api_shares_report_active_market_events_analyse():
    api_report(f'{config.api_url}/api/shares/report/active-market-events-analyse',
        { "tickerList": 'shares/watchlist' })


def test_api_shares_report_asset_report_events():
    api_report(f'{config.api_url}/api/shares/report/asset-report-events',
        { "tickerList": 'shares/watchlist' })


def test_api_shares_report_fear_greed_index():
    api_report(f'{config.api_url}/api/shares/diagram/fear-greed-index',
        { "tickerList": 'shares/watchlist' })


def test_api_shares_diagram_daily_close_prices():
    api_diagram_simple(f'{config.api_url}/api/shares/diagram/daily-close-prices',
        { "from": fromDate, "to": toDate, "tickerList": 'shares/watchlist' })


def test_api_shares_diagram_five_minutes_close_prices():
    api_diagram_simple(f'{config.api_url}/api/shares/diagram/five-minutes-close-prices',
        { "from": fromDateTime, "to": toDateTime, "tickerList": 'shares/watchlist' })


def test_api_shares_diagram_multiplicators_mcap_pe_netdebtebitda():
    api_diagram_bubble(f'{config.api_url}/api/shares/report/multiplicators-mcap-pe-netdebtebitda',
        { "tickerList": 'shares/watchlist' })
