from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from .views import (
    LoginAPIView, RegisterAPIView,UserInformationAndPatchingRetrieveAPIView,
    UserInformationAndPatchingListView, 
    UserStatusesListView, UserStatusesRetrieveAPIView,
    company_cheсk, itn_search
    # PasswordRestoreAPIView
)

urlpatterns = [
    path('users/', UserInformationAndPatchingListView.as_view()),

    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('profile/changes/<int:pk>', UserInformationAndPatchingRetrieveAPIView.as_view(), name='user_progile_changing'),

    path('statuses/', UserStatusesListView.as_view()),
    path('statuses/<int:pk>', UserStatusesRetrieveAPIView.as_view()),

    path('users/', UserInformationAndPatchingListView.as_view()),
    path('users/<uuid:pk>/', UserInformationAndPatchingRetrieveAPIView.as_view()),

    # path('password/restore/start/', StartingPasswordRestoreAPIView.as_view()),
    # path('password/restore/', PasswordRestoreAPIView.as_view()),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    path('uploads/company/', company_cheсk),
    path('users/search/', itn_search),

]
