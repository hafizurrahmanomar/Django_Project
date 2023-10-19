

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('blog/',include('Blog.urls')),
    path('html/',include('HTML.urls')),
    path('css/',include('CSS.urls')),
    path('python/',include('Python.urls')),
    path('javascript/',include('JavaScript.urls')),
    path('java/',include('Java.urls')),
    path('django/',include('Django.urls')),
    path('comments/',include('Comments.urls')),
    path('author/',include('Author.urls')),
    

]


    
    
    
    
    
   
   