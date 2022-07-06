from datetime import date
from django.http import HttpResponse
from django.shortcuts import render

data = {
    "movies": [
        {
          "title": "film 1 adı",
          "description": "açıklama",
          "imageUrl": "m1.jpg",
          "coverImage": "cover1.jpg",
          "slug":"film-adi-1",
          "language": "english",
          "date": date(2022,1,2)
        },
         {
          "title": "film 2 adı",
          "description": "açıklama",
          "imageUrl": "m2.jpg",
          "coverImage": "cover2.jpg",
          "slug":"film-adi-2",
          "language": "english",
          "date": date(2022,1,3)
        },
         {
          "title": "film 3 adı",
          "description": "açıklama",
          "imageUrl": "m3.jpg",
          "coverImage": "cover3.jpg",
          "slug":"film-adi-3",
          "language": "english",
          "date": date(2022,1,4)
        },
         {
          "title": "film 4 adı",
          "description": "açıklama",
          "imageUrl": "m4.jpg",
          "slug":"film-adi-4",
          "language": "english",
          "date": date(2022,4,2)
        }
    ],
    "sliders": [
        {
        "slider_image":"slider1.jpg",
        "url":"film-adi-1"
        },
         {
        "slider_image":"slider2.jpg",
        "url":"film-adi-2"
        },
         {
        "slider_image":"slider3.jpg",
        "url":"film-adi-3"
        }
    ]
}

def index(request):
    movies = data["movies"]
    sliders = data["sliders"]
    return render(request, 'index.html', {
        "movies": movies,
        "sliders":sliders

    }) 

def movies(request):
    movies = data["movies"]
    return render(request, 'movies.html', {
        "movies": movies
    })


def movie_details(request, slug):
    movies = data["movies"]
    selectedMovie = None
    for movie in movies:
        if movie["slug"] == slug:
            selectedMovie = movie

    return render(request, 'movie-details.html', {
        "movie": selectedMovie
    })

# return render("details:"+ slug)