from pickle import TRUE
from rest_framework.views import APIView
from rest_framework import viewsets, status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from users.permissions import IsMember, IsLibrarian
from users.serializers import UserRegistrationSerializer, UserDeactivateSerializer
from .models import Books
from .serializers import BookSerializer, MemberSerializer

User = get_user_model()


class ShowBooksview(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)


class AddBookView(generics.CreateAPIView):
    queryset = Books.objects.all()
    model = Books
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsLibrarian)


class UpdateBookView(generics.UpdateAPIView):
    queryset = Books.objects.all()
    lookup_field = "id"
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsLibrarian)


class RemoveBookView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    lookup_field = "id"
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsLibrarian)


class ShowAllMembersView(generics.ListAPIView):
    queryset = User.objects.filter(role='member', is_active=True)
    serializer_class = MemberSerializer
    permission_classes = (IsAuthenticated, IsLibrarian)


class AddMemberView(APIView):
    permission_classes = (IsAuthenticated, IsLibrarian)
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = request.data.get('username')
            name = request.data.get('password')
            password = request.data.get('password')

            user = User.objects.create(
                username=username,
                name=name,
                role='member',
            )

            user.set_password(password)
            user.save()

            content = {
                'username': user.username,
                'name': user.name,
                'role': user.role
            }

            response_content = {
                'status': True,
                'message': 'User Added successfully.',
                'result': content
            }

            return Response(response_content, status=status.HTTP_200_OK)
        else:
            response_content = {
                'status': False,
                'message': 'Unable to create user.',
                'result': serializer.errors
            }

            return Response(response_content, status=status.HTTP_400_BAD_REQUEST)


class UpdateMemberView(generics.UpdateAPIView):
    queryset = User.objects.all()
    lookup_url_kwarg = "id"
    serializer_class = MemberSerializer
    permission_classes = (IsAuthenticated, IsLibrarian)


class RemoveMemberView(APIView):
    permission_classes = (IsAuthenticated, IsLibrarian)
    serializer_class = UserDeactivateSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']

            user = User.objects.get(id=user_id)
            user.is_active = False
            user.save()

            content = {
                'username': user.username,
                'name': user.name,
                'role': user.role
            }

            response_content = {
                'status': True,
                'message': 'User removed successfully.',
                'result': content
            }

            return Response(response_content, status=status.HTTP_200_OK)
        else:
            response_content = {
                'status': False,
                'message': 'Unable to remove user.',
                'result': serializer.errors
            }

            return Response(response_content, status=status.HTTP_400_BAD_REQUEST)


class ShowBorrowedBooksView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsMember)

    def get_queryset(self):
        books = Books.objects.filter(borrower=self.request.user)
        return books


class BorrowBookview(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsMember)

    def update(self, request, *args, **kwargs):
        user = request.user
        book_id = kwargs['id']

        book = Books.objects.get(id=book_id)

        if book.availability_status == 'borrowed':
            return Response('Book is not available.', status=status.HTTP_400_BAD_REQUEST)
        
        book.availability_status = 'borrowed'
        book.borrower = user
        book.save()

        response_content = {
            'status': True,
            'message': 'Book successfully borrowed',
            'result': book.name
        }

        return Response(response_content)

class ReturnBookview(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated, IsMember)

    def update(self, request, *args, **kwargs):
        user = request.user
        book_id = kwargs['id']

        book = Books.objects.get(id=book_id)

        book.availability_status = 'available'
        book.borrower = None
        book.save()

        response_content = {
            'status': True,
            'message': 'Book successfully returned',
            'result': book.name
        }

        return Response(response_content)
