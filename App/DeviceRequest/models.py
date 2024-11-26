from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
user = get_user_model()

class device(models.Model):
    device_name = models.CharField(max_length=150)
    device_status = models.BooleanField(default=False)

    def __str__(self):
        return self.device_name

class DeviceRequestAccess(models.Model):
    requestee = models.ForeignKey(user, on_delete=models.CASCADE)
    device = models.ForeignKey(device, on_delete=models.DO_NOTHING)
    dateRequested = models.DateField()
    dateTobeUsed = models.DateField()
    accessDuration = models.IntegerField()
    requestStatus = models.BooleanField(default=False)

class AccessRequestHistory(models.Model):
    accessid = models.ForeignKey(DeviceRequestAccess, on_delete=models.CASCADE)
    dateapproved = models.DateTimeField(auto_now_add=True)
    