from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Author, Category


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'status', 'created_at')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Category)