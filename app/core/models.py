from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from core.utils import content_file_name




class MyProfile(models.Model):
    """User Profile Details"""
    position = models.CharField(max_length=254, default="guest", blank=True)
    image = models.ImageField(upload_to=content_file_name, default="portraits/default.jpg")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return str(self.owner) + " profile"




class ModuleModel(models.Model):
    """Model for Module"""
    phase_title = models.CharField(max_length=254, default="Not Specified", blank=True)
    module_title = models.CharField(max_length=254, default="Not Specified", blank=True)
    module_brand = models.CharField(max_length=254, default="Not Specified", blank=True)
    module_file_type = models.CharField(max_length=254, default="Not Specified", blank=True)
    module_link = models.CharField(max_length=254, default="Not Specified", blank=True)
    counter_dict = models.TextField(default="Not Specified")
    budget = models.IntegerField(blank=False, default=0)
    budget_difference = models.IntegerField(blank=False, default=0)
    budget_adjustment = models.IntegerField(blank=False, default=0)
    revision = models.IntegerField(blank=False, default=0)
    year = models.IntegerField(blank=False, default=0)
    month = models.IntegerField(blank=False, default=0)
    week = models.IntegerField(blank=False, default=0)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Modules"

    def __str__(self):
        return str(self.phase_title) + " " + str(self.year) + " " + str(self.month) + " " + str(self.week)
