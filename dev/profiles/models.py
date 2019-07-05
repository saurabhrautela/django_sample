from django.db import models
# `AbstractBaseUser` and `PermissionMixin` are base classes used for customizing the Django User Model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# `BaseUserManager` is extended by custom user manager to customize how users are created from Django CLI
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles."""

    def create_user(self, email, name, password=None):
        """Create a new user profile."""
        if not email:
            raise ValueError("User must have an email address.")

        # normalize email to change the second half of email to lowercase as it is not case-sensitive
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user with given details."""
        user = self.create_user(email=email, name=name, password=password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # `is_active` field is used to determine if a user's profile is activated
    is_active = models.BooleanField(default=True)
    # `is_staff` determines if a user should have access to django admin
    is_staff = models.BooleanField(default=False)

    # Specify model manager to be used for the objects
    # This is need to work with UserModel in Django CLI so that it knows how to create and control users
    objects = UserProfileManager()

    # Override `USERNAME_FIELD` to user `email` instead of `username` for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of the user."""
        return self.name

    def get_short_name(self):
        """Retrieve short name of the user."""
        return self.name

    def __str__(self):
        """Return string representation of the user."""
        return self.email
