from django.shortcuts import render

# Create your views here.

def myPython(request):
    return render(request,'Python/index.html')
