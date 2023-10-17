from django.urls import path


from . import views

#import views here

urlpatterns = [
    path('author/',views.myAuthor,name='author'),
    
]