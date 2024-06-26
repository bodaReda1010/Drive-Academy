from django.shortcuts import render
from . models import Course
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='accounts:login')
def course(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request , 'course/course.html', context)
