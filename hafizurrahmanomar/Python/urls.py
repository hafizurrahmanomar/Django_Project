from django.urls import path


from . import views

#import views here

urlpatterns = [
    path('python/',views.myPython,name='python')
]