from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
	fieldsets = [
        ('Post Title', {'fields': ['title_text']}),
        ('Post Content', {'fields': ['content_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Post, PostAdmin)