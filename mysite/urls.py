from django.urls import path
from api.views import sum, hi


urlpatterns = [
    path('sum/', sum),
    path('hi/<name>', hi)
]
