from django.urls import path


from . import views

#import views here

urlpatterns = [
    path('java/',views.myJava,name='java')
]