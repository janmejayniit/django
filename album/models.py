from django.db import models
from django.db.models.query import QuerySet
# from django.contrib.auth.models import User
from authuser.models import User
from django.utils.html import mark_safe
from django.db.models.signals import post_save


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

    def image_tag(self):
        return mark_safe('<a href="/images/%s" target="_blank"><img src="/images/%s" width="250" height="150" /></a>' % (self.image,self.image))
    image_tag.short_description = 'Image'



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
    
class AlbumLikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name="likedislikes", related_query_name='likedislike', on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'album')
    



""" def albumCreate(sender, instance, **kwargs):
    print("Album created")

post_save.connect(albumCreate, sender=Album) """