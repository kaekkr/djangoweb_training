from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    text = "Data"
    return render(request, "./index.html", {
        'text': text
    })
