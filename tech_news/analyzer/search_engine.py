from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    tuple_list = []
    noticias = search_news({"title": {'$regex': title, '$options': 'i'}})
    for noticia in noticias:
        tuple_list.append((noticia["title"], noticia["url"]))
    return tuple_list
    # https://www.mongodb.com/community/forums/t/case-insensitive-search-with-regex/120598


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
