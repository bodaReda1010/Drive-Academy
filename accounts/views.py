from django.shortcuts import render , redirect
from . models import Account , User
from . forms import LoginForm , RegisterForm , ProfileForm , UserForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse




def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request , user)
            return redirect('accounts:profile')
        else:
            return HttpResponse('Please Enter At Least All Data Without Image')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html' , {'form': form,})



def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username = username , password = password)
            login(request , user)
            return redirect('accounts:profile')
        else:
            return HttpResponse('Please Enter Your Username And Password')
    else:
        login_form = LoginForm()

    return render(request , 'accounts/login.html' , {'login_form': login_form,})



def profile(request):
    return render(request , 'accounts/profile.html')



def logout_view(request):
    logout(request)
    return redirect('accounts:login')




def edit_profile(request):
    account = Account.objects.get(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST,request.FILES,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=account)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:profile')
    else:

        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=account)

    context = {
        'user_form':user_form,
        'profile_form' :profile_form,
    }
    return render(request,'accounts/edit_profile.html',context)




def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        if confirm_password == password:
            user_exists = User.objects.filter(email = email).exists()
            if user_exists:
                user = User.objects.get(email = email)
                user.set_password(password)
                user.save()
                return redirect('accounts:profile')
            else:
                return HttpResponse('This E-mail Is Not Exsists')
        else:
            return HttpResponse('Please Enter Password Equal To Reset Password')
        
    return render(request , 'accounts/reset_password.html')