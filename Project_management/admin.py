from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Self_details)
class Register_Self(admin.ModelAdmin):
    list_display = ['name', 'landline1', "company_mail", 'datetime']


@admin.register(models.About_us)
class Register_Self(admin.ModelAdmin):
    list_display = ['name', 'long_description', 'datetime']


@admin.register(models.Service_name)
class Service_Register(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(models.Service_item)
class Register_item_resgister(admin.ModelAdmin):
    list_display = ['name', 'short_description', 'image']


@admin.register(models.Team_name)
class Register_team_name_resgister(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(models.Team_members)
class Register_team_name_resgister(admin.ModelAdmin):
    list_display = ['name', 'job_title', 'facebook']


@admin.register(models.Customer_Messages)
class Register_customer_message(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject' ]
