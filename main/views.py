from django.shortcuts import render
from .models import Band


def main_page(request):
    data = Band.objects.all()
    print()
    print(data)
    print()
    return render(request, 'main/index_main.html', {'data': data})


def band_page(request, genre, slug):
    data = Band.objects.filter(genre=genre).get(slug=slug)
    return render(request, 'main/index_band.html', {'data': data})


def about_page(request, genre):
    data = Band.objects.filter(genre=genre)
    return render(request, 'main/index_about.html', {'data': data})


