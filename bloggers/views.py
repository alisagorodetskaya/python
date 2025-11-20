
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .data import BloggerData
from .news_data import NewsData

data = BloggerData()
news_data = NewsData()

def home(request):
    html = "<h1>Головна сторінка</h1><p>Актуальні новини блогерів</p>"
    html += '<a href="/profiles/">Список блогерів</a> | <a href="/news/">Новини</a>'
    return HttpResponse(html)

def profiles(request):
    bloggers = data.get_all_bloggers()
    html = "<h1>Список блогерів</h1><table border='1'><tr><th>Ім'я</th><th>Категорія</th><th>Опис</th></tr>"
    for b in bloggers:
        html += f"<tr><td><a href='/profiles/{b['id']}/'>{b['name']}</a></td><td>{b['category']}</td><td>{b['description']}</td></tr>"
    html += "</table><p><a href='/'>На головну</a></p>"
    return HttpResponse(html)

def profile_detail(request, blogger_id):
    blogger = data.get_blogger_by_id(int(blogger_id))
    if not blogger:
        return HttpResponse("<h1>404 Not Found</h1>", status=404)
    html = f"<h1>{blogger['name']}</h1><p>Категорія: {blogger['category']}</p><p>{blogger['description']}</p>"
    html += "<p>Соцмережі:</p><ul>"
    for key, link in blogger["social"].items():
        html += f"<li><a href='{link}' target='_blank'>{key}</a></li>"
    html += "</ul><p><a href='/profiles/'>Назад</a></p>"
    return HttpResponse(html)

def news(request):
    news_list = news_data.get_all_news()
    html = "<h1>Останні новини блогерів</h1>"
    html += "<table border='1'><tr><th>Заголовок</th><th>Джерело</th></tr>"
    for n in news_list:
        html += f"<tr><td><a href='{n['link']}' target='_blank'>{n['title']}</a></td><td>{n['source']}</td></tr>"
    html += "</table><p><a href='/'>На головну</a> | <a href='/profiles/'>Список блогерів</a></p>"
    return HttpResponse(html)


