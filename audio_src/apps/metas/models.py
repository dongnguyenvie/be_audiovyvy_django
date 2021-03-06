import json
from django.db import models
import uuid


class Meta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jsonLd = models.TextField(blank=True, default=json.dumps({}))
    # type = models.CharField(max_length=10, db_index=True, null=True)
    view = models.BigIntegerField(default=0)
    like = models.BigIntegerField(default=0)
    # Generator
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.id)

    # def delete()
