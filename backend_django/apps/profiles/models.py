from email.policy import default
import imp
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from phonenumbers import PhoneNumber

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")

class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+254795941990")
    about_me = models.TextField(verbose_name=_("About me"), default="Say something about yourself")
    Image = models.ImageField(verbose_name=_("Profile Picture"), default="/profile_default.jpg")
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=10)
    country = CountryField(verbose_name=_("Country"), default="KE", blank=False, null=False)
    city = models.CharField(verbose_name=_("City"), max_length=100, default="Nairobi", blank=False, null=False)
    is_buyer = models.BooleanField(verbose_name=_("Buyer"), default=False, help_text=_("Are you looking to buy a property"))
    is_seller = models.BooleanField(verbose_name=_("Seller"), default=False, help_text=_("Are you looking to sella property"))
    is_agent = models.BooleanField(verbose_name=_("Agent"), default=False, help_text=_("Are you an agent"))
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(verbose_name=_("Reviews"), default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
