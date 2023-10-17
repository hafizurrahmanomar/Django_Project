
from django.urls import path


from . import views

#import views here

urlpatterns = [
    path('',views.index,name='home'),
    path('home/',views.home)
]