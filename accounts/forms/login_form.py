from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label=_('Username'),
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'autocomplete': 'off',
                'class': 'form-control',
                'placeholder': 'Entre seu utilizador',
            }
        ),
    )

    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'current-password',
                'placeholder': 'Entre a palavra-passe',
                'class': 'form-control',
            }
        ),
    )
