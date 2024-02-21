from django.contrib import admin
from . import models


class ForumMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'total_threads', 'total_posts', 'date_joined']
    list_display_links = ['user']
    fieldsets = (
        ("Member info:".title(), {
            "fields": (
                'user', 'skills', 'avatar', 
            ),
        }),
    )
    
    
    def total_threads(self, obj: models.ForumMember):
        return obj.user.threads.count()
    total_threads.short_description = 'Total Threads'
    
    def total_posts(self, obj: models.ForumMember):
        return obj.user.posts.count()
    total_posts.short_description = 'Total Posts'


class ThreadAdmin(admin.ModelAdmin):
    list_display = ['creator', 'title', 'created_at']

class PostAdmin(admin.ModelAdmin):
    list_display = ['thread', 'author', 'created_at']

    



admin.site.register(models.ForumMember, ForumMemberAdmin)
admin.site.register(models.Thread, ThreadAdmin)
admin.site.register(models.Post, PostAdmin)
