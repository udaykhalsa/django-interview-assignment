from django.urls import path
from .views import *


urlpatterns = [
    path('api/show-books/', ShowBooksBview.as_view(), name='add_book'),
    path('api/add-book/', AddBookView.as_view(), name='add_book'),
    path('api/update-book/<int:id>/', UpdateBookView.as_view(), name='update_book'),
    path('api/remove-book/<int:id>/', RemoveBookView.as_view(), name='remove_book'),
]
