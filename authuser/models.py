from django.core.checks import messages
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150, null=True)
    email = models.CharField(max_length=150, unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, upload_to='avatar/')

    # USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return  self.username.title()

class Followers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    follow_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fuser')
    receive_notification = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):        
        if self.user != self.follow_user:
            return super().save(*args, **kwargs)
        else:
            # self.message_user( "Follow and Follower should be different", level=messages.ERROR) 
            # raise Exception("Follow and Follower should be different")
            raise ValidationError("Follow and Follower should be different")

    class Meta:
        unique_together = ('user', 'follow_user')
        # verbose_name = "follower"
        verbose_name_plural  = "followers"
    
