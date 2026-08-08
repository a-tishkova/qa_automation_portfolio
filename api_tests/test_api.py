import requests


def test_api_connection():
    url = "https://httpbin.org"
    response = requests.get(url)
    
    assert response.status_code == 200

