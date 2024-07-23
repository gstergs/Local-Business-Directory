from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('is_user', css_class='form-check-input'),
            Field('is_admin', css_class='form-check-input'),
            Submit('submit', 'Sign up', css_class='btn btn-primary')
        )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'is_user', 'is_admin')

class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('is_user', css_class='form-check-input'),
            Field('is_admin', css_class='form-check-input'),
            Submit('submit', 'Update', css_class='btn btn-primary')
        )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'is_user', 'is_admin')

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=63, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)
