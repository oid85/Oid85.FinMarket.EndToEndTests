import config
from modules.api_tests import api_list_tickers, api_report_datarange_tickerlist, api_report_tickerlist, api_diagram_simple, api_diagram_bubble


def test_api_shares_watch_list_tickers():
    api_list_tickers(f'{config.api_url}/api/shares/watch-list-tickers')


def test_api_shares_report_aggregated_analyse():
    api_report_datarange_tickerlist(f'{config.api_url}/api/shares/report/aggregated-analyse', 'shares/watchlist')


def test_api_shares_report_supertrend_analyse():
    api_report_datarange_tickerlist(f'{config.api_url}/api/shares/report/supertrend-analyse', 'shares/watchlist')


def test_api_shares_report_candle_sequence_analyse():
    api_report_datarange_tickerlist(f'{config.api_url}/api/shares/report/candle-sequence-analyse', 'shares/watchlist')


def test_api_shares_report_candle_volume_analyse():
    api_report_datarange_tickerlist(f'{config.api_url}/api/shares/report/candle-volume-analyse', 'shares/watchlist')


def test_api_shares_report_rsi_analyse():
    api_report_datarange_tickerlist(f'{config.api_url}/api/shares/report/rsi-analyse', 'shares/watchlist')


def test_api_shares_report_atr_analyse():
    api_report_datarange_tickerlist(f'{config.api_url}/api/shares/report/atr-analyse', 'shares/watchlist')


def test_api_shares_report_donchian_analyse():
    api_report_datarange_tickerlist(f'{config.api_url}/api/shares/report/donchian-analyse', 'shares/watchlist')


def test_api_shares_report_yield_ltm_analyse():
    api_report_datarange_tickerlist(f'{config.api_url}/api/shares/report/yield-ltm-analyse', 'shares/watchlist')


def test_api_shares_report_drawdown_from_maximum_analyse():
    api_report_datarange_tickerlist(f'{config.api_url}/api/shares/report/drawdown-from-maximum-analyse', 'shares/watchlist')


def test_api_shares_report_dividend_analyse():
    api_report_tickerlist(f'{config.api_url}/api/shares/report/dividend-analyse', 'shares/watchlist')


def test_api_shares_report_multiplicator_analyse():
    api_report_tickerlist(f'{config.api_url}/api/shares/report/multiplicator-analyse', 'shares/watchlist')


def test_api_shares_report_forecast_target_analyse():
    api_report_tickerlist(f'{config.api_url}/api/shares/report/forecast-target-analyse', 'shares/watchlist')


def test_api_shares_report_forecast_consensus_analyse():
    api_report_tickerlist(f'{config.api_url}/api/shares/report/forecast-consensus-analyse', 'shares/watchlist')


def test_api_shares_report_active_market_events_analyse():
    api_report_tickerlist(f'{config.api_url}/api/shares/report/active-market-events-analyse', 'shares/watchlist')


def test_api_shares_report_asset_report_events():
    api_report_tickerlist(f'{config.api_url}/api/shares/report/asset-report-events', 'shares/watchlist')


def test_api_shares_report_fear_greed_index():
    api_report_tickerlist(f'{config.api_url}/api/shares/diagram/fear-greed-index', 'shares/watchlist')


def test_api_shares_diagram_daily_close_prices():
    api_diagram_simple(f'{config.api_url}/api/shares/diagram/daily-close-prices', 'shares/watchlist')


def test_api_shares_diagram_five_minutes_close_prices():
    api_diagram_simple(f'{config.api_url}/api/shares/diagram/five-minutes-close-prices', 'shares/watchlist')


def test_api_shares_diagram_multiplicators_mcap_pe_netdebtebitda():
    api_diagram_bubble(f'{config.api_url}/api/shares/report/multiplicators-mcap-pe-netdebtebitda', 'shares/watchlist')
