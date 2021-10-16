from django.contrib import admin
from .models import User, Followers
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(User)
admin.site.unregister(Group)

@admin.register(Followers)
class FollowerAdmin(admin.ModelAdmin):

    list_display= ('user', 'follow_user', 'receive_notification', 'created_date',)