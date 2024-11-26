from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import os

user = get_user_model()
# Create your models here.

def validate_zip(value):
    """Validator to ensure the uploaded file is a ZIP."""
    ext = os.path.splitext(value.name)[1]
    if ext.lower() != '.zip':
        raise ValidationError("Only ZIP files are allowed.")

class DataEntry(models.Model):
    owner = models.ForeignKey(user, on_delete = models.CASCADE)
    location = models.CharField(max_length=255, help_text="Entry name")
    csv = models.FileField(upload_to='uploads/zips/', validators=[validate_zip], blank=False, null=False)
    videos = models.FileField(upload_to='uploads/zips/', validators=[validate_zip], blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner.email
