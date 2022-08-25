from tech_news.database import create_news
import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url: str, wait: int = 3) -> str:
    try:
        response = requests.get(
            url, timeout=wait, headers={"user-agent": "Fake user-agent"}
        )
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
def scrape_next_page_link(html_content: str) -> str or None:
    selector = Selector(html_content)
    next_page = selector.css('a.next.page-numbers::attr(href)').get()
    if next_page:
        return next_page
    else:
        return None


# Requisito 4
def scrape_noticia(html_content: str) -> dict:
    selector = Selector(html_content)
    noticia = {
        "url": "",
        "title": "",
        "timestamp": "",
        "writer": "",
        "comments_count": 0,
        "summary": "",
        "tags": [],
        "category": ""
    }
    url = selector.xpath("//link[@rel='canonical']/@href").get()
    title = selector.css('h1.entry-title::text').get()
    timestamp = selector.css('li.meta-date::text').get()
    writer = selector.css('a.url.fn.n::text').get()
    coments_count = len(
        selector.xpath('//li[starts-with(@id, "comment")]').getall()
    )
    sumary = "".join(
        selector.css('div.entry-content').css('p')[0].css('::text').getall()
    )
    tags = selector.xpath('//a[contains(@rel, "tag")]').css('::text').getall()
    category = selector.css('span.label::text').get()
    noticia.update({
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": coments_count,
        "summary": sumary.strip(),
        "tags": tags,
        "category": category
    })
    return noticia


# Requisito 5
def get_tech_news(amount: int) -> list:
    count = 0
    next_page = "https://blog.betrybe.com/"
    dict_list = []
    while next_page and count < amount:
        response = fetch(next_page)
        links = scrape_novidades(response)
        for link in links:
            if count >= amount:
                break
            content = fetch(link)
            dict = scrape_noticia(content)
            dict_list.append(dict)
            count += 1
        next_page = scrape_next_page_link(response)
    create_news(dict_list)
    return dict_list
