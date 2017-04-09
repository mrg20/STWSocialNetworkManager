from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

'''
This models.py isn't a final one. Maybe we do some changes
later on.

We are deciding if we are going to extend django user model.
'''

class Network(models.Model):
    name = models.TextField(null = False)
    description = models.TextField()


class Complement(models.Model):
    type = models.TextField(max_length=300)
    id_network = models.ForeignKey(Network)
    description = models.TextField()


class Box(models.Model):
    id_user = models.ForeignKey(User, default=1)
    box_num = models.IntegerField(null=False)
    network = models.ForeignKey(Network, null=False)
    complement = models.ForeignKey(Complement, null=False)