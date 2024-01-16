from django.urls import path


from . import views

#import views here

urlpatterns = [
    path('comments/',views.myComments,name='comments')
]