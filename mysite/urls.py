from django.urls import path
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:

    if request.method == 'GET':
        a = request.GET.get('a')
        b = request.GET.get('b')

        result = int(a) + int(b)

    return HttpResponse(f"{a} + {b} = {result}")


urlpatterns = [
    path('home/', index)
]
