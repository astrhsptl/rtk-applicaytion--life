from django.urls import path

from .views import (
    ApplicationStatusListView, ApplicationStatusRetrieveAPIView,
    ApplicationServiceListView, ApplicationServiceRetrieveAPIView,
    ApplicationListView, ApplicationRetrieveAPIView, application_cheсk,
    ApplicationStateListView, ApplicationStateRetrieveAPIView
)

urlpatterns = [
    path('status/', ApplicationStatusListView.as_view()),
    path('status/<int:pk>/', ApplicationStatusRetrieveAPIView.as_view()),

    path('state/', ApplicationStateListView.as_view()),
    path('state/<int:pk>/', ApplicationStateRetrieveAPIView.as_view()),

    path('service/', ApplicationServiceListView.as_view()),
    path('service/<int:pk>/', ApplicationServiceRetrieveAPIView.as_view()),


    path('', ApplicationListView.as_view()),
    path('<uuid:pk>/', ApplicationRetrieveAPIView.as_view()),

    path('check/', application_cheсk),
]
