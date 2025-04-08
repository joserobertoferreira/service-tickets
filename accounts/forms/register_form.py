from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser


class RegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }

    vat_number = forms.CharField(
        max_length=20,
        required=True,
        label=_('VAT Number'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Informe o número de contribuinte',
                'autocomplete': 'off',
            }
        ),
    )

    password1 = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Entre a palavra-passe',
                'class': 'form-control',
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_('Password confirmation'),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Entre a palavra-passe',
                'class': 'form-control',
            }
        ),
        help_text=_('Enter the same password as before, for verification.'),
    )

    first_name = forms.CharField(
        max_length=45,
        required=True,
        label=_('Name'),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    last_name = forms.CharField(
        max_length=45,
        required=True,
        label=_('Surname'),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    email = forms.EmailField(
        max_length=254,
        required=True,
        label=_('Email'),
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )

    username = UsernameField(
        max_length=5,
        required=True,
        label=_('Username'),
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'autocomplete': 'off',
                'class': 'form-control',
                'placeholder': 'Entre seu utilizador',
            }
        ),
        help_text=_('Required. Username must be between 3 and 5 characters long'),
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'vat_number', 'password1', 'password2')

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if len(username) < 3 or len(username) > 5:  # noqa: PLR2004
    #         raise forms.ValidationError('Username must be between 3 and 5 characters long')
    #     return username

    def save(self, commit=True):
        user = super().save(commit=False)

        user.vat_number = user.vat_number.upper()
        user.username = user.username.upper()

        if commit:
            user.save()

        return user
