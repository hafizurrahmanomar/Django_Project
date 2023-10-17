from django.shortcuts import render

# Create your views here.
def home(request):
    #context={}
    return render(request,'Home/home.html')

def index(request):
    return render(request,'Home/index.html')