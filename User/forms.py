from django import forms


class UserLogin(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(
        max_length=20, required=True, widget=forms.PasswordInput())
