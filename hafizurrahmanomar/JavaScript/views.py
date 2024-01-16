from django.shortcuts import render


# Create your views here.
def myJavaScript(request):
    return render(request,'JavaScript/index.html')