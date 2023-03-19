from django.urls import path

from .views import AddChange


urlpatterns = [
    path('make/', AddChange.as_view()),
]
