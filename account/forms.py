from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.core.exceptions import ValidationError

def validate_nith(value):
    if "@nith.ac.in" in value:
        return value
    else:
        raise ValidationError("Please enter institute ID only!")

class Register(UserCreationForm):
    email = forms.EmailField(validators=[validate_nith])

    class Meta:
        model = User
        fields = [ 'email']

