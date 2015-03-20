# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library

from django.db import models
from django.conf import settings
# from django.utils.translation import ugettext_lazy as _


# Subclass AbstractUser
class User(AbstractUser):

    def __unicode__(self):
        return self.username


class Preference(models.Model):
    setting = models.CharField(max_length=128)
    value = models.TextField()

    class Meta:
        db_table = 'userprofile_preference'

    def __unicode__(self):
        return "%s=%s" % (self.setting, self.value)


class UserProfile(models.Model):
    # TODO: should this get changed?
    #
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile")
    preferences = models.ManyToManyField(Preference,
                                         blank=True,
                                         db_table='userprofile_userprofile_preferences')

    class Meta:
        db_table = 'userprofile_userprofile'

    def __unicode__(self):
        return "%s" % self.user