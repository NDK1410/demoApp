from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
	fieldsets = [
        ('Post Title', {'fields': ['title_text']}),
        ('Post Content', {'fields': ['content_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

	list_display = ('title_text', 'content_text', 'pub_date')
	list_filter = ('pub_date',)
	search_fields = [('title_text', 'content_text')]

admin.site.register(Post, PostAdmin)