from django.shortcuts import render
#Custom Import
from Blog.models import MyBlogPost

#Custom Import
from Blog import forms



# Create your views here.
def pythonblog(request):
    
    course_name ='Python Masster Class A to z'
    mentor_name = 'Hafizur Rahman Omar'
    totall_class = 100
    course_duration = "2.5 month's"
    course_details = {'courseName':course_name,'mentorName':mentor_name,'totallClass':totall_class,'courseDuration':course_duration}
    
    return render(request,'Blog/python.html',context=course_details)




def tag(request):
    
    context= {  'course_name':'JavaScript Masster Class A to z',
                'mentor_name':'Hafizur Rahman Omar',
                'totall_class':'200',
                'course_duration':" 6 month's "
            }
    
    return render(request,'Blog/tag.html',context)


def forLoop(request):
    
    cityName ={'name':['Dhaka','Pabna','Sylet','Bogura','Tangail'] }
    
    return render(request,'Blog/forLoop.html',context=cityName)
    
   
def myStatic(request):
    return render(request,'Blog/static.html' ) 

# very importent part in the below

def myBlog(request):
    #blogs = MyBlogPost.object.all()
    return render(request,'Blog/index.html',{} )        
    
    
def blog_details(request,blog_id):
    blog = MyBlogPost.objects.get(id=blog_id)
    return render(request,'Blog/blog_details.html',{'blog_dtetails':blog})


# Django Forms View code here

def myDjangForm(request):
    #DjangoForm=>NameForm object create=>DjangoForm
    DjangoForm = forms.NameForm()
    my_dictionary={"django_form":DjangoForm,"heading": "This Forms Create by Django Libary"}
    return render(request, 'Blog/form.html',context=my_dictionary)
        
 
