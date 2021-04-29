from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


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
    categories = Category.objects.all()
    context = {
        'news': news, 
        'title' : 'Список новостей',
        'categories': categories,
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id = category_id )
    categories = Category.objects.all()
    category = Category.objects.get(pk = category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category})