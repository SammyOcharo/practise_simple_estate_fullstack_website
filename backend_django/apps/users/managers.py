from ast import Not
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise (_('You must provide a valid email'))
    

    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        if not username:
            raise ValueError(_('Users must submit a username'))
        if not first_name:
            raise ValueError(_('Users must submit a first name'))
        if not last_name:
            raise ValueError(_('Users must submit a last name'))
        
        if email:
            email = self.normalize_email
            self.email_validator(email)
        else:
            raise ValidationError(_('Base User Account: An email address is required'))
        

        user = self.model(
            username=username,
            first_name = first_name,
            last_name = last_name,
            email = email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff")is not True:
            raise ValueError (_('Superusers must have is_staff True'))

        if extra_fields.get("is_super")is not True:
            raise ValueError (_('Superusers must have is_super True'))

        if not password:
            raise ValueError(_('super users must submit a password'))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Admin Account: An email address is required'))


        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)

        user.save(using=self._db)

        return user