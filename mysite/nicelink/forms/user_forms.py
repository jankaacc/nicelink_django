from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django import forms

from ..models.User import UserModel


class UserRegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password']

    def clean(self):
        # cleaned_data = super(UserForm, self).clean()
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

# User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Incorrect Username or password")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect Username or password")
        return super(UserLoginForm, self).clean(*args, **kwargs)




