from django.shortcuts import render


# Create your views here.
def myDjango(request):
    return render(request,'Django/index.html')