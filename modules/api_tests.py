import requests
from datetime import datetime, timedelta


def api_list_tickers(url):
    # arrange
    # act
    response = requests.get(url)
    response_json = response.json()
    result = response_json["result"]

    # assert
    assert response.status_code == 200
    assert len(result) > 0


def api_report_datarange_tickerlist(url, tickerList):
    # arrange
    toDate = datetime.now()
    fromDate = toDate - timedelta(days=7)

    body = {
        "from": fromDate.strftime('%Y-%m-%d'),
        "to": toDate.strftime('%Y-%m-%d'),
        "tickerList": tickerList
    }

    # act
    response = requests.post(url, json=body)
    response_json = response.json()
    result = response_json["result"]

    title = result["title"]
    header = result["header"]
    data = result["data"]

    # assert
    assert response.status_code == 200
    assert len(title) > 0
    assert len(header) > 0
    assert len(data) > 0


def api_report_tickerlist(url, tickerList):
    # arrange
    body = {
        "tickerList": tickerList
    }

    # act
    response = requests.post(url, json=body)
    response_json = response.json()
    result = response_json["result"]

    title = result["title"]
    header = result["header"]
    data = result["data"]

    # assert
    assert response.status_code == 200
    assert len(title) > 0
    assert len(header) > 0
    assert len(data) > 0


def api_diagram_close_prices(url, tickerList):
    # arrange
    toDate = datetime.now()
    fromDate = toDate - timedelta(days=7)

    body = {
        "from": fromDate.strftime('%Y-%m-%d'),
        "to": toDate.strftime('%Y-%m-%d'),
        "tickerList": tickerList
    }

    # act
    response = requests.post(url, json=body)
    response_json = response.json()
    result = response_json["result"]

    title = result["title"]
    data = result["data"]

    # assert
    assert response.status_code == 200
    assert len(title) > 0
    assert len(data) > 0


def api_diagram_multiplicators(url, tickerList):
    # arrange
    body = {
        "tickerList": tickerList
    }

    # act
    response = requests.post(url, json=body)
    response_json = response.json()
    result = response_json["result"]

    title = result["title"]
    series = result["series"]

    # assert
    assert response.status_code == 200
    assert len(title) > 0
    assert len(series) > 0