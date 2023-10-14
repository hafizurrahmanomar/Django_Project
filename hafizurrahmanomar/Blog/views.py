from django.shortcuts import render

# Create your views here.
def pythonblog(request):
    
    course_name ='Python Masster Class A to z'
    mentor_name = 'Hafizur Rahman Omar'
    totall_class = 100
    course_duration = "2.5 month's"
    course_details = {'courseName':course_name,'mentorName':mentor_name,'totallClass':totall_class,'courseDuration':course_duration}
    
    return render(request,'Blog/python.html',context=course_details)
