from django.urls import path
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:

    if request.method == 'GET':
        name = request.GET.get('name')
        print(name)

    return HttpResponse(f"Salom {name}")


urlpatterns = [
    path('home/', index)
]
