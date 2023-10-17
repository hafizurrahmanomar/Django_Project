from django.urls import path


from . import views

#import views here

urlpatterns = [
    path('html/',views.myHTML,name='html')
]