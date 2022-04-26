from django import forms


class LoginForm(forms.Form):
    Username = forms.CharField(max_length=50)
    Password = forms.CharField(max_length=12, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    Username = forms.CharField(max_length=15, min_length=8, label="Username")
    Email = forms.EmailField(max_length=254, label="Email Address")
    Password1 = forms.CharField(
        min_length=8,
        max_length=12,
        label="Enter your Password",
        widget=forms.PasswordInput,
    )
    Password2 = forms.CharField(
        min_length=8,
        max_length=12,
        label="Enter your Password again",
        widget=forms.PasswordInput,
    )
