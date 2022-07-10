from django.urls import path
from .views import AddMemberView, UpdateMemberView, UserRegistrationView, UserLoginView


urlpatterns = [
    path('api/user-signup/', UserRegistrationView.as_view(), name='user_signup'),
    path('api/user-login/', UserLoginView.as_view(), name='user_signup'),

    path('api/add-member/', AddMemberView.as_view(), name='add_member'),
    path('api/add-member/', UpdateMemberView.as_view(), name='add_member'),
]
