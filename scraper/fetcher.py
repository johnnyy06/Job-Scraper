import requests
from bs4 import BeautifulSoup


def get_url(template, location, position):
    url = template.format(location, position)
    return url


def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        raise Exception(f"Failed to fetch page: {response.status_code}")
