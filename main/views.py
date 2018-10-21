from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import New


def home(request):
    item = New.objects.filter(main=1).last()
    context = {
        'last': item
    }
    return render(request, 'home.html', context=context)


class NewsList(ListView):
    model = New
    queryset = New.objects.filter(main=0).order_by('id')
    template_name = 'pages/news.html'
    context_object_name = 'articles'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        item = New.objects.filter(main=1).last()

        context = super().get_context_data(**kwargs)
        context['last'] = item
        print(dir(context['articles']))
        return context
