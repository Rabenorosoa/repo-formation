from django.contrib import admin
from .models import PostModel
from django.contrib.auth.models import Group

class PostModelAdmin(admin.ModelAdmin):
    search_fields = ('title', 'content')

admin.site.register(PostModel,PostModelAdmin)
admin.site.unregister(Group)
admin.site.site_header = 'Post Management'
admin.site.site_title = 'Post Management'
