from django.contrib import admin
from .models import device, DeviceRequestAccess, AccessRequestHistory
# Register your models here.
admin.site.register(device)
admin.site.register(DeviceRequestAccess)
admin.site.register(AccessRequestHistory)