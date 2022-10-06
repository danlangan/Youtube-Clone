from cgi import print_exception
from unicodedata import decimal
from django.db import models
from authentication.models import User

# Create your models here.

class Comment(models.Model):
    video_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)