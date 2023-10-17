from django.urls import path


from . import views

#import views here

urlpatterns = [
    path('django/',views.myDjango,name='django')
]