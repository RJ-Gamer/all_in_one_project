"""
Choice classes for users app
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class GenderChoiceField(models.TextChoices):
    """
    Gender Choices for users
    """

    OTHER = _("Other"), "Other"
    MALE = _("Male"), "Male"
    FEMALE = _("Female"), "Female"
