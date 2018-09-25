from django.contrib import admin

from .models import RfidDB
from .models import Status

# Register your models here.


admin.site.register(RfidDB)
admin.site.register(Status)
