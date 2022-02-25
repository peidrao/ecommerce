from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))
 
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'password')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        password2= cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('Password does not match')


        return super().clean()

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
       
        self.fields['first_name'].widget.attrs['placeholder'] = 'Your First name' 
        self.fields['last_name'].widget.attrs['placeholder'] = 'Your Last name' 
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email' 
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Your Phone Number' 
  
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

