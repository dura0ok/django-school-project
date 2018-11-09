from django.core.mail import send_mail
from django.shortcuts import render, redirect
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


def ask(request):

    if request.method == "POST":
        #print(request.POST)
        name = request.POST.get('name')
        mail = request.POST.get('email')
        subject = request.POST.get('subject')
        print(name, mail)
        comment = request.POST.get('comment')
        st = 'Вам письмо от ' + name + ' Его почта: ' + mail + '\n' + comment
        st = str(st)
        print(st)
        send_mail(subject, st, 'fenixrnd@mail.ru', ['fenixrnd1@mail.ru'])
        return redirect('/success')
    result = Menu.objects.all().order_by('sort')
    context = {
        'menu': result

    }
    return render(request, 'pages/ask.html', context=context)


def success(request):
    return render(request, 'pages/success.html')