from django.shortcuts import render

# Create your views here.
def myHTML(request):
    return render(request,'HTML/index.html')