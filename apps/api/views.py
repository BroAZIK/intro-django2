from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest) -> HttpResponse:

    return HttpResponse(f"API")


def about(request: HttpRequest) -> HttpResponse:

    return HttpResponse(f"Hi")
    