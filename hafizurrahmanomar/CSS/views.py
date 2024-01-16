from django.shortcuts import render

# Create your views here.
def myCSS(request):
    return render(request,'CSS/index.html')
