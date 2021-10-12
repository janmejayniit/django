from django.contrib import admin
from .models import Contest,Prize,Album,Winner,Comment


# Register your models here.
admin.site.register(Contest)
admin.site.register(Prize)
admin.site.register(Album)
admin.site.register(Winner)
admin.site.register(Comment)

""" @admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fields = ['user', 'image', 'is_active'] """


