from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.PostUser)
admin.site.register(models.Post)
