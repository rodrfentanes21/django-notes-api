from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create new user profile"""
        if not email:
            raise ValueError('User must have an email adress')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save new superuser"""
        user = self.create_user(email, name, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for user, containing attributes (id, name, email, password)"""
    # this class does not explicitally declares the id attribute because i will be using the Django's base id.
    email = models.EmailField(max_length=255, unique=True)
    user_id = id
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        """Returns the name associated to the account"""
        return self.name
    
    def __str__(self):
        """Returns the email associated to the account"""
        return self.email


class NoteManager(models.Manager):

    def create(self, title, body, user_id=None):
        """Create a new note with the specified user ID, title, and body."""
        note = self.model(
            user_id=user_id,
            title=title,
            body=body,
        )
        note.save()
        return note

    def update(self, note, title, body):
        """Update the specified note with the specified title and body."""
        note.title = title
        note.body = body
        note.save()



class Note(models.Model):
    """Database model for user, containing attributes (id, user_id, title, body, created_at, updated_at)"""
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=1000)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = NoteManager()