from django import forms
from . models import Account , User
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']



class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields  = '__all__'        
        exclude = 'user',


