from django.contrib.auth.models import User
from .models import Author
from django.db.models.signals import post_save  # Type of signal
from django.dispatch import receiver

# User is created -> signal -> Author
# Author(signal) -> Author is created for new User


@receiver(post_save, sender=User)
def create_user_author(sender, instance, created, **kwargs):
    # sender - the model
    # instance - the model's instance (that was created or saved, User(username='yossi', pass..))
    # created - True if the instance was created, False if the instance was already in the db
    if created:  # if the user was just created
        Author.objects.create(user=instance, name=instance.username)
