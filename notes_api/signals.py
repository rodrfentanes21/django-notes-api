from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Note, UserProfile

@receiver(post_save, sender=Note)
def set_user_id(sender, instance, created, **kwargs):
    """Set the user ID of the newly created note to the ID of the user who created it."""
    if created:
        instance.user_id = instance.created_by.id
        instance.save()