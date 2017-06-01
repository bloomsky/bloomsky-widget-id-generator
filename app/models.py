from __future__ import unicode_literals

from django.db import models

import string, random

# Create your models here.
class IDReference(models.Model):
    device_id = models.CharField(primary_key=True, unique=True, max_length=12)
    widget_id = models.CharField(unique=True, max_length=8, blank=True, null=True)


    # override the save method and generate random 8-digit widget id
    def save(self, *args, **kwargs):
        if not self.widget_id:
            id_parts = []
            id_parts.extend(random.sample(string.uppercase, 2))
            id_parts.extend(random.sample(string.digits, 2))
            id_parts.extend(random.sample(string.lowercase, 2))
            id_parts.extend(random.sample(string.hexdigits, 2))

            ordered_parts = ''.join(id_parts)
            new_id = ''.join(random.sample(ordered_parts, len(ordered_parts)))

            self.widget_id = new_id
        super(IDReference, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.device_id
