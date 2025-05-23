from django.db import models

class Member(models.Model):
    user_name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return self.user_name


