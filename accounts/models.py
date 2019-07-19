from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.core.validators import RegexValidator
from django.shortcuts import reverse
from PIL import Image


USERNAME_INVALID =\
    'Usersname must be alphanumber and consist of 5 characters or more'
EMAIL_REQUIRED = 'Users must have an email address'


class UserManager(BaseUserManager):
    """
    User model Manager to handle user Creation and several other User
    related methods.
    """

    def _create_user(
            self, username, email, password, is_staff, is_active,
            is_superuser, **extra_fields):
        """
        Base function for user creation
        """
        if not email:
            raise ValueError(EMAIL_REQUIRED)
        user = self.model(username=username, email=email,
            is_staff=is_staff, is_active=is_active, is_superuser=is_superuser,
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        user.save()
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        """
        Creates non-superuser args are passed to the main _create function
        """
        is_staff, is_superuser, is_active = False, False, False
        args = (username, email, password, is_staff, is_active, is_superuser)
        return self._create_user(*args, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        """
        Creates superuser args are passed to the main _create function
        """
        is_active = is_staff = is_superuser = True
        args = (username, email, password, is_staff, is_active, is_superuser)
        return self._create_user(*args, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64, default='')
    last_name = models.CharField(max_length=64, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'username',

    def __str__(self):
        """
        String representation of a user object
        """
        return self.username

    def get_absolute_url(self):
        """
        User unique URL
        """
        return reverse('home')

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=250, default=' ', blank=True)

    def __str__(self):
        return '{} Profile'.format(self.user.username)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)
