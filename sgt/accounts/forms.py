from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
)

from .models import UserDbv


class CustomUserDbvCreationForm(UserCreationForm):
    """A form for creating new users.
        Includes all the required fields, plus a repeated password.
    """

    class Meta(UserCreationForm.Meta):
        model = UserDbv
        fields = ('username', 'email')

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            UserDbv._default_manager.get(username=username)
        except UserDbv.DoesNotExist:
            return username
        raise forms.ValidationError('Error username')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomUserDbvChangeForm(UserChangeForm):

    password = ReadOnlyPasswordHashField(
        label='password',
        help_text='Your password is encrypted.'
    )

    class Meta(UserChangeForm.Meta):
        model = UserDbv
        fields = (
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'age',
            'profile_image',
            'group',
            'position'
        )

    def clean_password(self):
        return self.initial['password']


class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    username = forms.CharField(
        widget=forms.widgets.TextInput, label="username")
    email = forms.EmailField(widget=forms.widgets.TextInput, label="Email")
    password1 = forms.CharField(
        widget=forms.widgets.PasswordInput,
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.widgets.PasswordInput,
        label="Password (again)"
    )

    class Meta:
        model = UserDbv
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()``
        because it applies to more than one field.
        """
        self.cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(
                    "Passwords don't match. Please enter both fields again."
                )
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class AuthenticationForm(forms.Form):
    """
    Login form
    """
    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        fields = ['email', 'password']
