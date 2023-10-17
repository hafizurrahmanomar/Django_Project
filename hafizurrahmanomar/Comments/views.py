from django.shortcuts import render

# Create your views here.
def myComments(request):
    return render(request,'Comments/index.html' )  