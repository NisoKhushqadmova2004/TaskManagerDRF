from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.EmailField(max_length=100)
    password_hash = models.CharField()
    full_name = models.CharField(max_length=80)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

