import requests


def test_api_connection():
    url = "https://tinkoff.ru"
    response = requests.get(url, verify=False)
    
    assert response.status_code == 200


