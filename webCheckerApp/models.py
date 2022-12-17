from django.db import models
from django.utils.timezone import now
# Create your models here

class User(models.Model):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=16,default=None)
    user_created_at = models.DateTimeField(default=now())

class WebsiteModel(models.Model):
    url = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete = models.CASCADE,default = 1)
    total_likes = models.IntegerField(default=0)
    total_dislikes = models.IntegerField(default=0)

class Like(models.Model):
    like_or_dislike = models.IntegerField(default=0)
    website = models.ForeignKey(WebsiteModel, on_delete = models.CASCADE,default=1)
    user = models.ForeignKey(User, on_delete = models.CASCADE,default=1)
