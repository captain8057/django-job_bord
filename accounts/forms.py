from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile




class SignupForm(UserCreationForm):
   class Meta:
        model = User
        fields = ['username','email','password1','password2']




class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]


class ProfileForm(ModelForm):
    class Meta:
       model = profile
       fields = ["phone_number","city_name","image"]
       
        
