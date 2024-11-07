from django.shortcuts import render

from .models import *

def main(request):
    title = RanobeTitle.objects.all()

    queryset = {
        'title':title
    }

    return render(request, 'main/index.html', queryset)


def book_page(request):
    return render(request, 'main/book-page.html')
