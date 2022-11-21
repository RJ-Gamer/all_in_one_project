"""
User model
"""
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
from users.managers import UserManager
from users.choices import GenderChoiceField


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model
    """

    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("Email"), max_length=100, db_index=True, unique=True)
    first_name = models.CharField(
        _("First Name"), max_length=100, null=True, blank=True
    )
    last_name = models.CharField(_("Last Name"), max_length=100, null=True, blank=True)
    gender = models.CharField(
        _("Gender"),
        max_length=100,
        choices=GenderChoiceField.choices,
        null=True,
        blank=True,
    )
    profile_image = models.ImageField(
        _("Profile Image"), null=True, blank=True, upload_to="profile_images"
    )

    is_active = models.BooleanField(_("Is Active"), default=False)
    is_staff = models.BooleanField(_("Is Staff"), default=False)
    is_superuser = models.BooleanField(_("Is Superuser"), default=False)

    created_at = models.DateTimeField(
        _("Created At"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:
        """
        Returns a string representation of the user.
        """
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm: str, obj=None) -> bool:
        """
        Returns True if the user has the specified perm for given obj.
        """
        return super().has_perm(perm, obj)

    def has_module_perms(self, app_label: str) -> bool:
        """
        Returns True if the user has the permission to access the given module.
        """
        return super().has_module_perms(app_label)
