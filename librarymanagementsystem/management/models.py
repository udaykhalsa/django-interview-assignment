from secrets import choice
from django.db import models

AVAILABILITY_STATUS = (
    ('borrowed', 'Borrowed'),
    ('available', 'Available')
)
class Books(models.Model):
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    availability_status = models.CharField(max_length=26, choices=AVAILABILITY_STATUS, default='available')
    borrower = models.CharField(max_length=26, null=True)
