from tech_news.database import search_news
import datetime


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
    try:
        data = datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    formated_date = data.strftime("%d/%m/%Y")
    print(formated_date)
    tuple_list = []
    noticias = search_news({"timestamp": formated_date})
    for noticia in noticias:
        tuple_list.append((noticia["title"], noticia["url"]))
    return tuple_list
# https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python


# Requisito 8
def search_by_tag(tag):
    tuple_list = []
    noticias = search_news(
        {"tags": {'$elemMatch': {'$regex': tag, '$options': 'i'}}}
    )
    for noticia in noticias:
        if (noticia not in tuple_list):
            tuple_list.append((noticia["title"], noticia["url"]))
    return tuple_list


# Requisito 9
def search_by_category(category):
    tuple_list = []
    noticias = search_news(
        {"category": {'$regex': category, '$options': 'i'}}
    )
    for noticia in noticias:
        if (noticia not in tuple_list):
            tuple_list.append((noticia["title"], noticia["url"]))
    return tuple_list
