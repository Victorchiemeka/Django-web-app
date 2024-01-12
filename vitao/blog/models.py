from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class POST(models.Model):
    title = models.CharField(max_length=100)  # max_length is required
    content = models.TextField()  # trd: text field
    date_posted = models.DateTimeField(
        default=timezone.now
    )  # timezone.now is a function, not a function call
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # on_delete: if user is deleted, delete the post as well

    def __str__(self):
        return self.title
