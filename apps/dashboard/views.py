from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest) -> HttpResponse:

    return HttpResponse(f"Dashboard")


def about(request: HttpRequest, name: str) -> HttpResponse:

    return HttpResponse(f"About")
    