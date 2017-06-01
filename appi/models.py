from __future__ import unicode_literals
from django.db import models
from django.conf import settings
# Create your models here.

class SkyDevice(models.Model):
    """The database storing the camera DeviceID
    and bounded user name and other device information, used as the device
    authentication and functional database"""
    DeviceID = models.CharField(max_length=12, primary_key=True, unique=True)
    LatestFWVersion1 = models.CharField(max_length=14, default='0.0.0')
    LatestFWVersion2 = models.CharField(max_length=14, default='0.0.0')
    LAT = models.FloatField(default=0)
    LON = models.FloatField(default=0)
    ALT = models.FloatField(default=0)
    UTC = models.SmallIntegerField(default=0)
    DST = models.SmallIntegerField(default=0)
    Searchable = models.BooleanField(default=True)
    RegisterTime = models.PositiveIntegerField(default=0)
    CityName = models.CharField(max_length=200)
    StreetName = models.CharField(max_length=200)
    FullAddress = models.TextField()
    DeviceName = models.CharField(max_length=100)
    RainNotification = models.BooleanField(default=False)
    BatteryNotification = models.BooleanField(default=False)
    C_or_F = models.BooleanField(default=True)
    Tag = models.CharField(max_length=500, default='')
    Description = models.TextField(default='')

    def __unicode__(self):
        return self.DeviceID
