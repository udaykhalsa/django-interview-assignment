## Library Management System
In this project you can manage books and members in a library and also borrow
books as a member of the library.

## Dependencis
 - python3.10 (preferred)
 - Create a virtual environment.
 - Pip install all the packages mentioned 'requirements.txt' file.
 - Postman desktop support.

## Postman Collection
 - A postman collection is included in the repository for covinience and testing.
 - Run project with python manage.py runserver before testing with postman endpoints.

## Run Project
 - On linux/mac run project with 'python3 manage.py runserver'
 - On windows run project with 'python.exe manage.py runserver'
 - NOTE - make migrations before running project with upper commands'
 - Make migrations with 'python3 manage.py makemigrations'
 - Migrate/Sync to Database wth 'python3 manage.py migrate' 
 - The project will run on localhost i.e http://127.0.0.1 and port 8000 by default.
 - This can be changed by running 'manage.py runserver <port-number>'

## Project Endpoints
 - All project endpoints are mentioned in the Postman Collection for ease.