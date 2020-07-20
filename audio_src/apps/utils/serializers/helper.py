from rest_framework.serializers import ValidationError
from rest_framework import status, permissions
from audio_src.apps.utils.validator.extension_validation import BlogValidationError


def get_owner_and_blog(self, validated_data):
    owner = validated_data.pop('owner', None)
    blog = None if not owner else owner.user.blog
    if not blog:
        raise BlogValidationError()
    return [owner, blog]
