from django.urls import path

from . import views

#import views here

urlpatterns = [
    path('pythonblog/',views.pythonblog,name='pythonblog'),
    path('tag/',views.tag,name='tag'),
    path('forLoop/',views.forLoop,name='forLoop'),
    path('myStatic/',views.myStatic,name='myStatic'),
    
    # imporatant path
    path('myBlog/',views.myBlog,name='myBlog'),
    
    path('blog_details/<int:blog_id>/',views.blog_details,name='blog_details'),
    path('myDjangForm/',views.myDjangForm,name='myDjangForm')
]