from django.urls import path


from . import views

#import views here

urlpatterns = [
    path('pythonblog/',views.pythonblog,name='pythonblog')
]