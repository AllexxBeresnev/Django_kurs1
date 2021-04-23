from django.shortcuts import render
from django.http import HttpResponse

from .models import News


''' в качеастве параметра экземпляр класса запроса с заголовками и прочим,
соответственно, нужно что-нибудь вернуть 
'''
def index(request):
    #print(request.META)
#    res = '<h1>Список новостей</h1>'
#    for item in news:
#        res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>\n'
#    return HttpResponse(res)
    news = News.objects.order_by('-created_at') # но если в админке указали другой, то можно оставить all
    context = {
        'news': news, 
        'title' : 'Список новостей'
    }
    return render(request, 'news/index.html', context)

