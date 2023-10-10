from django.urls import path
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:

    return HttpResponse("Hello, world. You're at the index.")


urlpatterns = [
    path('home/', index)
]
