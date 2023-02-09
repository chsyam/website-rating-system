from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here


class WebsiteModel(models.Model):
    url = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    total_likes = models.IntegerField(default=0)
    total_dislikes = models.IntegerField(default=0)


class Like(models.Model):
    like_or_dislike = models.IntegerField(default=0)
    website = models.ForeignKey(
        WebsiteModel, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
