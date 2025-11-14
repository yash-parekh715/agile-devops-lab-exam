import requests

BASE_URL = "http://127.0.0.1:5000"


def test_status():
    res = requests.get(f"{BASE_URL}/status")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


def test_sum():
    res = requests.get(f"{BASE_URL}/sum?a=5&b=7")
    assert res.status_code == 200
    assert res.json() == {"sum": 12}


def test_sum_invalid():
    res = requests.get(f"{BASE_URL}/sum?a=abc&b=5")
    assert res.status_code == 400
