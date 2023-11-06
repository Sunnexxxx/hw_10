from django.shortcuts import render
from .models import Band, Genre


def main_page(request):
    data = Genre.objects.all()
    return render(request, 'main/index_main.html', {'data': data})


def band_page(request, genre, slug):
    find = Genre.objects.get(genre=genre).pk
    data = Band.objects.filter(genre=find).get(slug=slug)
    print()
    print(data)
    return render(request, 'main/index_band.html', {'data': data})


def about_page(request, genre):
    find = Genre.objects.get(genre=genre).pk
    data = Band.objects.filter(genre=find)
    return render(request, 'main/index_about.html', {'data': data})


