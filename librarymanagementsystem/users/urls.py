from django.urls import path
from .views import UserRegistrationView, UserLoginView


urlpatterns = [
    path('api/user-signup/', UserRegistrationView.as_view(), name='user_signup'),
    path('api/user-login/', UserLoginView.as_view(), name='user_signup'),
]
