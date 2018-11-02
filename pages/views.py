from django.shortcuts import render
from .models import Page, Menu
# Create your views here.


def home(request):
    return render(request, 'home.html')


def show_page(request, id):
    result = Menu.objects.all().order_by('sort')
    page = Page.objects.get(id=id)
    context = {
        'page': page,
        'menu': result
    }
    return render(request, 'pages/page.html', context=context)