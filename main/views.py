from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import New
from pages.models import Menu


def home(request):
    menu_list = Menu.objects.all().order_by('sort')
    item = New.objects.filter(main=1).last()
    context = {
        'last': item,
        'menu': menu_list
    }
    return render(request, 'home.html', context=context)


class NewsList(ListView):
    model = New
    queryset = New.objects.filter(main=0).order_by('id')
    template_name = 'pages/news.html'
    context_object_name = 'articles'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        item = New.objects.filter(main=1).last()
        menu_list = Menu.objects.all().order_by('sort')
        context = super().get_context_data(**kwargs)
        context['last'] = item
        context['menu'] = menu_list
        return context


class Detail(DetailView):
    model = New
    context_object_name = 'article'
    template_name = 'pages/post.html'

    def get_context_data(self, **kwargs):
        menu_list = Menu.objects.all().order_by('sort')
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_list
        return context


