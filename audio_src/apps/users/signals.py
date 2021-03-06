from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from audio_src.apps.users.models import CustomUser

MEMBER_GROUP = 'member'
@receiver(post_save, sender=CustomUser)
def add_to_default_group(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        group = Group.objects.get_or_create(name=MEMBER_GROUP)[0]
        user.groups.add(group.id)
