from django.urls import path
from .views import *


urlpatterns = [
    # View, Add, Update and Remove Books
    path('api/show-books/', ShowBooksview.as_view(), name='add_book'),
    path('api/add-book/', AddBookView.as_view(), name='add_book'),
    path('api/update-book/<int:id>/',
         UpdateBookView.as_view(), name='update_book'),
    path('api/remove-book/<int:id>/',
         RemoveBookView.as_view(), name='remove_book'),

    # View, Add, Update and Remove Member
    path('api/all-member/', ShowAllMembersView.as_view(), name='show_member'),
    path('api/add-member/', AddMemberView.as_view(), name='add_member'),
    path('api/update-member/<int:id>/', UpdateMemberView.as_view(), name='update_member'),
    path('api/remove-member/', RemoveMemberView.as_view(), name='remove_member'),

    # Borrow and Return Books
    path('api/show-borrowed-books/', ShowBorrowedBooksView.as_view(), name='borrow_book'),
    path('api/borrow-book/<int:id>/', BorrowBookview.as_view(), name='borrow_book'),
    path('api/return-book/<int:id>/', ReturnBookview.as_view(), name='borrow_book')
]
