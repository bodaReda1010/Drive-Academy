from django.shortcuts import render , redirect
from . models import Comment , Appointment
from accounts.models import Account
from django.contrib.auth.decorators import login_required
from course.models import Course
from django.http import HttpResponse
# Create your views here.


@login_required(login_url='accounts:login')
def write_comment(request):
    account = Account.objects.get(user = request.user)
    if request.method == 'POST':
        comment = request.POST['comment']
        profession = request.POST['profession']
        Comment.objects.create(
            account=account,
            comment=comment,
            profession=profession
        )
        return redirect('home')
    return render(request , 'pages/testimonial/comment.html')


@login_required(login_url='accounts:login')
def testimonial(request):
    comments = Comment.objects.all()
    context = {
        'comments':comments,
    }
    return render(request , 'pages/testimonial/testimonial.html' , context)




@login_required(login_url='accounts:login')
def features(request):
    return render(request, 'pages/features/features.html')


@login_required(login_url='accounts:login')
def appointment(request):
    if request.method == 'POST':
        try:
            name = Account.objects.get(user = request.user)
            car_type = request.POST['car_type']
            message = request.POST['message']
            course = Course.objects.get(name = request.POST['course'])
            Appointment.objects.create(
                name = name,
                email = name.user.email,
                course_name = course,
                car_type = car_type,
                message = message
            )
            return redirect('home')
        except:
            return HttpResponse('Please Enter The Name Of The Course Correctly')
    return render(request , 'pages/appointment/appointment.html')