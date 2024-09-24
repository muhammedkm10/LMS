from django import forms
from .models import CustomUser


# signup validation backend

class SignupForm(forms.Form):
    
    # taking data
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(), required=True)
    
    # username validation
    def clean_username(self):
        username = self.cleaned_data['username']
        if username == "" :
            print(username)
            raise forms.ValidationError("Username already exists")
        return username
    
    # email validation
    def clean_email(self):
        email = self.cleaned_data['email']
        if "@" not in email or CustomUser.objects.filter(email=email).exists(): 
            raise forms.ValidationError("Please enter a validemail address")
        return email
    
    # password validation
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

