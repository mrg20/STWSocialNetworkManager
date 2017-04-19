from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


'''
This models.py isn't a final one. Maybe we do some changes
later on.

We are deciding if we are going to extend django user model.
'''


class Network(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.TextField(max_length=300)
    network_url = models.URLField(null=False)

    def __unicode__(self):
        return self.name


class Complement(models.Model):
    type = models.CharField(max_length=20, null=False)
    id_network = models.ForeignKey(Network)
    description = models.TextField(max_length=300)

    def __unicode__(self):
        return self.type + " Network: " + self.id_network.name


class Box(models.Model):
    user = models.ForeignKey(User, default=1)
    box_num = models.IntegerField(null=False)
    network = models.ForeignKey(Network, null=False)
    complement = models.ForeignKey(Complement, null=False)
    logged_into_network = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.name + " Box: " + self.box_num
