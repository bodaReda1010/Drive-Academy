from django.shortcuts import render
from . models import Trainer
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='accounts:login')
def trainer(request):
    trainers = Trainer.objects.all()
    context = {
        'trainers':trainers,
    }
    return render(request , 'trainers/trainers.html' , context)
