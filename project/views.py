from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from course.models import Course
from trainers.models import Trainer
from pages.models import Comment



@login_required(login_url='accounts:login')
def home(request):
    courses = Course.objects.all()
    trainers = Trainer.objects.all()
    comments = Comment.objects.all()
    context = {
        'courses': courses,
        'trainers': trainers,
        'comments': comments,
    }
    return render(request , 'home/home.html' , context)