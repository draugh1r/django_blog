from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelBase
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.conf import settings

# Create your models here.

STATUS = (
    (0,"On_review"),
    (1,"Published")
)

class Post(models.Model):
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     title = models.CharField(max_length=200)
     slug = models.SlugField(max_length=200, unique=True, default=0)  #serve a fare un regex per indicizzare bene il titolo e renderlo ez to read
     text = models.TextField()
     created_date = models.DateTimeField(default=timezone.now)
     published_date = models.DateTimeField(blank=True, null=True)
     status = models.IntegerField(choices=STATUS, default=0)

     def publish(self):
         self.published_date = timezone.now()
         self.save()

     def __str__(self):
         return self.title
