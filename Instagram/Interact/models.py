from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#
#from
# class Followers(models.Model):
#     uuid=models.UUIDField(primary_key=True)
#
# class Users(models.Model):
#     uuid=models.UUIDField(primary_key=True)
#     username=models.CharField(max_length=20,unique=True)
#     email=models.EmailField()
#     password=models.CharField(max_length=20)
#     followers=models.ManyToManyField(Followers)
#
#     class Meta:
#         db_table='users'
#

class Uploads(models.Model):
    images=models.ImageField()
    videos=models.FileField()


class Profile(models.Model):
    user=models.ForeignKey(User,related_name='user',on_delete=models.CASCADE,unique=True)
    follows=models.ManyToManyField(User,related_name='followers',symmetrical=False)
    uploads=models.ManyToManyField(Uploads,related_name='uploads')

