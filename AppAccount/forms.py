from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import TextInput, PasswordInput
from django.utils.translation import gettext_lazy as _

from . import models


class UserSignupForm(UserCreationForm):
    ''' a custom form for signup '''
    class Meta:
        model = models.UserAccount
        fields = ("username", "password1", "password2")
        # get_user_model(): return the currently active user model – the custom user model if one is specified, or User otherwise.
        model = get_user_model()
   