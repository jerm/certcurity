from __future__ import unicode_literals

from django.db import models

class Cert(models.Model):
    owner = models.ForeignKey('accounts.', related_name='certs',
                    null=True, blank=True)
    cn = models.CharField(max_length=255, null=False, blank=False)
    fingerprint models.CharField(max_length=255, null=True, blank=True)
    create_datetime
    last_check_datetime
    
# Create your models here.
