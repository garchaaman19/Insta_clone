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
    images=models.ImageField(blank=True)
    videos=models.FileField(blank=True)


class Profile(models.Model):
    user=models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    follows=models.ManyToManyField(User,related_name='followers',symmetrical=False,blank=True,null=True)#symmetrical false means if user 1 is following user 2, then viceversa will not be automatically true unless user 2 follows user 1
    uploads=models.ManyToManyField(Uploads,related_name='uploads',blank=True)
    profile_pic = models.ImageField(upload_to='ProfilePicture/',default='/pics/GURMUKH DECORATIVE.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'



