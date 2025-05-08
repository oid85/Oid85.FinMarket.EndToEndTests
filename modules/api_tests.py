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


def api_report(url, tickerList):
    # arrange
    toDate = datetime.now()
    fromDate = toDate - timedelta(days=7)

    body = {
        "from": fromDate.strftime('%Y-%m-%d'),
        "to": toDate.strftime('%Y-%m-%d'),
        "tickerList": tickerList
    }

    # act
    response = requests.post(url, body)
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
