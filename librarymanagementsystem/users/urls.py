from django.urls import path
from .views import *


urlpatterns = [
    path('api/user-signup/', UserRegistrationView.as_view(), name='user_signup'),
    path('api/user-login/', UserLoginView.as_view(), name='user_signup'),
    path('api/deactivate-user/', UserDeactivateView.as_view(),
         name='deactivate_user'),
]
