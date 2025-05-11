import config
from datetime import datetime, timedelta
from modules.api_tests import api_list_tickers, api_report, api_diagram_simple, api_diagram_bubble


fromDate = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
toDate = datetime.now().strftime('%Y-%m-%d')


def test_api_bonds_filter_list_tickers():
    api_list_tickers(f'{config.api_url}/api/bonds/filter-list-tickers')

def test_api_bonds_watch_list_tickers():
    api_list_tickers(f'{config.api_url}/api/bonds/watch-list-tickers')
    
    
def test_api_bonds_report_aggregated_analyse():
    api_report(f'{config.api_url}/api/bonds/report/aggregated-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'bonds/watchlist' })


def test_api_bonds_report_supertrend_analyse():
    api_report(f'{config.api_url}/api/bonds/report/supertrend-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'bonds/watchlist' })
        
        
def test_api_bonds_report_candle_sequence_analyse():
    api_report(f'{config.api_url}/api/bonds/report/candle-sequence-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'bonds/watchlist' })


def test_api_bonds_report_candle_volume_analyse():
    api_report(f'{config.api_url}/api/bonds/report/candle-volume-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'bonds/watchlist' })


def test_api_bonds_report_atr_analyse():
    api_report(f'{config.api_url}/api/bonds/report/atr-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'bonds/watchlist' })


def test_api_bonds_report_donchian_analyse():
    api_report(f'{config.api_url}/api/bonds/report/donchian-analyse',
        { "from": fromDate, "to": toDate, "tickerList": 'bonds/watchlist' })


def test_api_bonds_report_coupon_analyse():
    api_report(f'{config.api_url}/api/bonds/report/coupon-analyse',
        { "tickerList": 'bonds/watchlist' })        
        
        
def test_api_bonds_bond_selection():
    api_list_tickers(f'{config.api_url}/api/bonds/report/bond-selection',
        {})        
    
    
def test_api_bonds_report_active_market_events_analyse():
    api_report(f'{config.api_url}/api/bonds/report/active-market-events-analyse',
        { "tickerList": 'bonds/watchlist' })


def test_api_bonds_diagram_daily_close_prices():
    api_diagram_simple(f'{config.api_url}/api/bonds/diagram/daily-close-prices',
        { "from": fromDate, "to": toDate, "tickerList": 'bonds/watchlist' })
        