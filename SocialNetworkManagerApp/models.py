from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Network(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    network_url = models.URLField()

    def __unicode__(self):
        return self.name


class Complement(models.Model):
    type = models.CharField(max_length=20)
    id_network = models.ForeignKey(Network)
    description = models.TextField(max_length=300)

    def __unicode__(self):
        return self.type + " Network: " + self.id_network.name


class Box(models.Model):
    user = models.ForeignKey(User, default=1)
    box_num = models.IntegerField()
    complement = models.ForeignKey(Complement)
    logged_into_network = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username + " Box: " + str(self.box_num)


class Incidence(models.Model):
    user = models.ForeignKey(User, default=1)
    network = models.CharField(max_length=30)
    explanation = models.TextField(max_length=300)
    date = models.DateField(default=now)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, default="")
    def __unicode__(self):
        return str(self.user) + " : " + str(self.network)


#Only used when the connections with the APIs are done
class UserNetworkInfo(models.Model):
    user = models.ForeignKey(User)
    network = models.ForeignKey(Network)
    network_username = models.CharField(max_length=50)
    network_password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.user.username + "   " + self.network.name
