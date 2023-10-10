from django.urls import path
from django.http import HttpResponse, HttpRequest


def sum(request: HttpRequest) -> HttpResponse:

    if request.method == 'GET':
        a = request.GET.get('a')
        b = request.GET.get('b')

        result = int(a) + int(b)

    return HttpResponse(f"{a} + {b} = {result}")

def hi(request: HttpRequest, name: str) -> HttpResponse:

    return HttpResponse(f"Hi {name}")


urlpatterns = [
    path('sum/', sum),
    path('hi/<name>', hi)
]
