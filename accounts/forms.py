from django.contrib.auth import password_validation
from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from .models import User, Profile


class UserCreationForm(BaseUserCreationForm):
    error_messages = {
        'password_mismatch': "The password didn't match",
    }

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean_first_name(self):
        username = self.cleaned_data.get('first_name').lower()
        return username

    def clean_last_name(self):
        username = self.cleaned_data.get('last_name').lower()
        return username

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def _post_clean(self):
        super()._post_clean()
        password = self.clean_password2()
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image',]
