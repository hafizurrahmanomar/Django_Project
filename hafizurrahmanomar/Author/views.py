from django.shortcuts import render

# Create your views here.

def myAuthor(request):
    return render(request,'Author/index.html')