import uuid

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, unique=True, default="Error")
    password = models.CharField(max_length=50, default="Error")
    age = models.IntegerField()

class Token(models.Model):
    key = models.CharField(max_length=40, unique=True)
    user = models.OneToOneField(User, related_name='auth_token', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        super().save(*args, **kwargs)

    def generate_key(self):
        return uuid.uuid4().hex