from django.db import models
from django.contrib.auth.models import User


class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    num_hours = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.num_hours} hours)'


# Create your models here.
class Capstone(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    # creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    expiry_date = models.DateField()
    topic = models.CharField(max_length=128)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

