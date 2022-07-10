from secrets import choice
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

AVAILABILITY_STATUS = (
    ('borrowed', 'Borrowed'),
    ('available', 'Available')
)
class Books(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    availability_status = models.CharField(max_length=26, choices=AVAILABILITY_STATUS, default='available')
    borrower = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
