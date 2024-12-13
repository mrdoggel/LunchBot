import requests

def get(url, params):
    return requests.get(url, params=params).text