import re

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=5,
        unique=True,
        help_text=_('Required. 5 characters or fewer. Letters and digits.'),
        validators=[
            validators.RegexValidator(re.compile(r'^[A-Za-z][A-Za-z0-9]*$'), _('Enter a valid username.'), _('invalid'))
        ],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
    first_name = models.CharField(_('first name'), max_length=45, blank=True)
    last_name = models.CharField(_('last name'), max_length=45, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    vat_number = models.CharField(
        _('vat number'),
        max_length=20,
        blank=True,
        help_text=_('VAT number of the user.'),
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'vat_number']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        """Return string representation of the user."""
        full_name = self.get_full_name()
        if full_name:
            return full_name
        return self.username

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
