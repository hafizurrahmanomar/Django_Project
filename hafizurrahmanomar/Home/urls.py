
from django.urls import path


from . import views

#import views here

urlpatterns = [
    path('',views.home,name='home')
]