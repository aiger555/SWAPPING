from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media',null=True, blank=False)