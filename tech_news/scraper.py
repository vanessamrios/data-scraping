import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url: str, wait: int = 3) -> str:
    try:
        response = requests.get(url, timeout=wait)
        time.sleep(1)
        if response.status_code != 200:
            response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content: str) -> list:
    selector = Selector(html_content)
    links = selector.css('a.cs-overlay-link::attr(href)').getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""

# inicia o projeto
