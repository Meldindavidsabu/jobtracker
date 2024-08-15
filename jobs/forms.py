# jobs/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Job, Company
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,  
            'password1': 'Your password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one digit. It cannot be entirely numeric.',
            'password2': 'Enter the same password as above, for verification.',
        }
        error_messages = {
            'password1': {
                'required': 'Please enter your password.',
                'min_length': 'Your password must be at least 8 characters long.',
                'password_mismatch': 'Your password must contain at least one uppercase letter, one lowercase letter, and one digit.',
            },
            'password2': {
                'required': 'Please confirm your password.',
                'invalid': 'The two password fields didn’t match.',
            },
        }

class JobForm(forms.ModelForm):
    company_name = forms.CharField(max_length=100, required=True, label='Company Name')
    resume = forms.FileField(required=False, label='Resume')
    cover_letter = forms.FileField(required=False, label='Cover Letter')
    portfolio = forms.FileField(required=False, label='Portfolio')

    class Meta:
        model = Job
        fields = ['title', 'description', 'company_name', 'application_date', 'status', 'resume', 'cover_letter', 'portfolio']
        widgets = {
            'application_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def save(self, commit=True):
        company_name = self.cleaned_data.pop('company_name')
        company, created = Company.objects.get_or_create(name=company_name)
        self.instance.company = company
        return super().save(commit)
