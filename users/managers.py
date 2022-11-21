"""
Manager for users that creates users and superusers.
"""
import logging
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

from common import constants

log = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    """
    Manager for users that creates users and superusers.
    """

    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email and password.

        parameters:
        ------------:
        email(str): The email address of the user
        password(str): The password for the user

        returns:
        -------------:
        User object
        """
        if not email:
            raise ValueError(_(constants.ERR_FIELD_REQUIRED.format("Email Address")))

        if not password:
            raise ValueError(_(constants.ERR_FIELD_REQUIRED.format("Password")))

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        log.info(constants.LOG_USER_CREATED.format(email))
        return user

    def create_superuser(self, email, password=None, **kwargs):
        """
        Creates and saves a superuser with the given email and password.

        parameters:
        ------------:
        email(str): The email address of the superuser
        password(str): The password for the superuser

        kwargs:
        -------------:
        is_superuser(bool): Whether user is a superuser. Default is True.
        is_staff(bool): Whether user is a staff member. Default is True.
        is_active(bool): Whether user is active. Default is True.

        returns:
        ------------:
        User object
        """
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_superuser") is not True:
            raise ValueError(
                _(constants.ERR_FLAG_REQUIRED.format("superuser", "is_superuser", True))
            )
        if kwargs.get("is_staff") is not True:
            raise ValueError(
                _(constants.ERR_FLAG_REQUIRED.format("staff", "is_staff", True))
            )
        if kwargs.get("is_active") is not True:
            raise ValueError(
                _(constants.ERR_FLAG_REQUIRED.format("user", "is_active", True))
            )
        return self.create_user(email, password, **kwargs)
