from django import forms
from .models import CustomUser


# signup validation backend

class AddCouseForm(forms.Form):
    
    # taking data
    name = forms.CharField(max_length=50)
    description   = forms.CharField(widget=forms.Textarea, max_length=500)
    
    # name validation
    def clean_name(self):
        name = self.cleaned_data['name']
        if name == "" :
            print(name)
            raise forms.ValidationError("name should be valid")
        return name
    
    # descriptioin validation
    def clean_description(self):
        description = self.cleaned_data['description']
        if description == "" or len(description) < 10:
            print(description)
            raise forms.ValidationError("description should be valid")
        return description
    
    

