from django.urls import path


from . import views

#import views here

urlpatterns = [
    path('css/',views.myCSS,name='css')
]