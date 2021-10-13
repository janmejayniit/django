from django.db import models
# from django.contrib.auth.models import User
from authuser.models import User
# Create your models here.

class Contest(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    banner = models.ImageField(upload_to='contest/')
    join_fee = models.DecimalField( max_digits=4, decimal_places=2, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    expired_at = models.DateField()
    is_active = models.BooleanField(default=True)

class Prize(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='prize')
    first_prize = models.CharField(max_length=150)
    second_prize = models.CharField(max_length=150)
    third_prize = models.CharField(max_length=150)

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='album')
    contest = models.ForeignKey(Contest, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    uploaded_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    

class Winner(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    award_date = models.DateField(auto_now_add=True)

class Comment(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(auto_now_add=True)
    



