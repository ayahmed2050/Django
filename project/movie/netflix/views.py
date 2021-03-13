from django.shortcuts import render, redirect
from . forms import movieForm
from . models import movies

# Create your views here.

def index(request):
    movie = movies.objects.all()
    return render(request, "netflix/index.html", {
        'movie': movie
    })

def create(request):
    form = movieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "netflix/create.html", {
        'form': form
    })


def show(request, id):
    movie = movies.objects.get(pk=id)
    return render(request, "netflix/show.html", {
        'movie': movie
    })


def update(request, id):
    movie = movies.objects.get(pk=id)
    form = movieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "netflix/update.html", {
        'form': form,
        'movie': movie
    })


def delete(request, id):
    movie = movies.objects.get(pk=id)
    movie.delete()
    return redirect("index")