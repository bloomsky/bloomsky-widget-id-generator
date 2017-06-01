import requests
from django.conf import settings
from appi.models import SkyDevice as SkyDeviceModel

class SkyDevice(object):

    @staticmethod
    def search_by_name(name):
        devices = SkyDeviceModel.objects.using('mysql').filter(DeviceName=name)
        return devices
