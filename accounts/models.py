from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    REQ_ROLE_CHOICES = (
        ('subscriber', 'Subscriber'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('editor', 'Editor'),
    )
    role = models.CharField(choices=REQ_ROLE_CHOICES, max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    approval = models.BooleanField(default=False)
    def __str__(self):
        return self.username
    class Meta:
        permissions = (
            ("view_user", "Can view user"),
            ("edit_user", "Can edit user"),
            ("delete_user", "Can delete user"),
            ("approve_user", "Can approve user"),
        )
