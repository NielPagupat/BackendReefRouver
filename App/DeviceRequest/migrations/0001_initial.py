# Generated by Django 5.1.3 on 2024-11-25 09:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=150)),
                ('device_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceRequestAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRequested', models.DateField()),
                ('dateTobeUsed', models.DateField()),
                ('accessDuration', models.IntegerField()),
                ('requestStatus', models.BooleanField(default=False)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='DeviceRequest.device')),
                ('requestee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccessRequestHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateapproved', models.DateTimeField(auto_now_add=True)),
                ('accessid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DeviceRequest.devicerequestaccess')),
            ],
        ),
    ]