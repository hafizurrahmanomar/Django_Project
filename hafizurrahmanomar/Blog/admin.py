from django.contrib import admin
#MyBlogPost Import
from .models import MyBlogPost

# Register your models here.

@admin.register(MyBlogPost)

class MyBlogPostAdmin(admin.ModelAdmin):
    list_display =('title','author','body',)


