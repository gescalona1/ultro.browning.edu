from django.contrib.auth.forms import UserCreationForm
from .models import Member
from django import forms
from django.core.exceptions import ValidationError
import datetime


class MemberCreationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'date_of_birth', 'graduation_year',
            'specialized', 'password'
        ]
        widgets = {
            'email': forms.TextInput(attrs={
                'style': 'text-transform:lowercase;'
            }),
            'password': forms.PasswordInput()
        }


class MemberLogForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={
                'style': 'text-transform:lowercase;'
            }),
            'password': forms.PasswordInput()
        }


"""
class MemberCreationForm(forms.Form):
  username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
  email = forms.EmailField(label='Enter email')
  date_of_birth = forms.DateBirth(label="Enter your date of birth", initial=datetime.date.today())
  graduation_year = forms.IntegerField(label="Enter your graduation year",
                                       initial=datetime.date.today().year,
                                       min_value=2000,
                                       max_value=3000
                                       )
  password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

  def clean_username(self):
    username = self.cleaned_data['username'].lower()
    r = User.objects.filter(username=username)
    if r.count():
      raise ValidationError("Username already exists")
    return username

  def clean_email(self):
    email = self.cleaned_data['email'].lower()
    r = User.objects.filter(email=email)
    if r.count():
      raise ValidationError("Email already exists")
    return email

  def clean_graduation_year(self):
    graduation_year = self.cleaned_data['graduation_year']
    current_year = datetime.datetime.today().year
    if current_year > graduation_year:
      raise ValidationError(f"Graduation year cannot be before {current_year}")
    return graduation_year

  def clean_password2(self):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')

    if password1 and password2 and password1 != password2:
      raise ValidationError("Password don't match")

    return password2

  def save(self, commit=True):
    user = User.objects.create_user(
      self.cleaned_data['username'],
      self.cleaned_data['email'],
      self.cleaned_data['date_of_birth'],
      self.cleaned_data['password1']
    )
    return user
"""
