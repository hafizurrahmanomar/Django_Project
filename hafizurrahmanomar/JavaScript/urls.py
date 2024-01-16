from django.urls import path


from . import views

#import views here

urlpatterns = [
    path('javascript/',views.myJavaScript,name='javascript')
]