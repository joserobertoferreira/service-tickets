# forms.py
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser


class ChangePasswordForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
        'invalid_username': _('This username is already taken.'),
    }

    user_name = UsernameField(
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

    new_password1 = forms.CharField(
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

    new_password2 = forms.CharField(
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    user_cache = None

    class Meta:
        model = CustomUser
        fields = ('user_name', 'new_password1', 'new_password2')

    def clean(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            self.add_error(
                'new_password2',
                ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                ),
            )

        # Validação adicional de força da senha
        try:
            if self.user_cache and new_password1:
                validate_password(new_password1, self.user_cache)
        except ValidationError as e:
            self.add_error(
                'new_password1',
                ValidationError(
                    str(e),
                    code='password_too_weak',
                ),
            )

        return super().clean()

    def clean_user_name(self):
        username = self.cleaned_data.get('user_name')

        self.user_cache = CustomUser.objects.filter(username__iexact=username).first()

        if not self.user_cache:
            self.add_error(
                'user_name',
                ValidationError(
                    self.error_messages['invalid_username'],
                    code='invalid_username',
                ),
            )

        return username

    def save(self, user):
        if user:
            password = self.cleaned_data['new_password1']
            user.set_password(password)  # Faz o hash automaticamente
            user.save()
            return user

        return None
