from django.db import models
from tinymce.models import HTMLField
import datetime
from autoslug import AutoSlugField


# Create your models here.
class Self_details(models.Model):
    name = models.CharField(max_length=500, default="", null=False)
    short_desc = models.CharField(max_length=500, default="", null=False, blank=True)
    long_desc = models.TextField(null=True, blank=True)
    manager_name = models.CharField(max_length=500, default="", null=True)
    landline1 = models.CharField(max_length=100, default="", null=False)
    landline2 = models.CharField(max_length=100, default="", null=True)
    mobile1 = models.CharField(max_length=100, default="", null=True)
    mobile2 = models.CharField(max_length=100, default="", null=True)
    personal_mail = models.EmailField(max_length=100, default="", null=True)
    company_mail = models.EmailField(max_length=100, default="", null=False)
    location_coordinates = models.CharField(max_length=100, default="", null=True)
    address = models.CharField(max_length=1000, default="", null=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    open_hours = models.CharField(max_length=100, default="", null=True,blank=True)
    twitter = models.CharField(max_length=2000, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=2000, null=True, blank=True)
    linkedin = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name


class About_us(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    short_desc = models.CharField(max_length=3000, null=True, blank=True)
    short_desc1 = models.CharField(max_length=3000, null=True, blank=True,
                                   default="add only if you need some extra description for ")
    long_description = HTMLField(null=True, blank=True,
                                 default='data you will insert here will be on the left side of page make sure to remove it or replace it')
    long_description_with_points = HTMLField(null=True, blank=True,
                                             default='data you will insert here will be on the right side of page make sure to remove it or replace it')
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Service_name(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Service_item(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='static/media')
    # slug = AutoSlugField(populate_from='name', null=True, blank=True, unique=True, max_length=700)


class Team_name(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Team_members(models.Model):
    profile_picture = models.ImageField(upload_to='static/profile_pics_team', blank=True, null=True)

    name = models.CharField(max_length=500, null=True, blank=True)
    job_title = models.CharField(max_length=500, null=True, blank=True)
    twitter = models.CharField(max_length=2000, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=2000, null=True, blank=True)
    linkedin = models.CharField(max_length=2000, null=True, blank=True)


class Customer_Messages(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    subject = models.CharField(max_length=500, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
