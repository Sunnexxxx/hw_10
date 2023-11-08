from django.shortcuts import render
from .models import Band


def main_page(request):
    context = Band.objects.all()
    data = set([i.genre for i in context])
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


