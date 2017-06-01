from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.core.urlresolvers import reverse
import json

from device import SkyDevice
from form import DeviceNameForm
from app.models import IDReference

# Create your views here.
class Search(View):

    # According to device name typed, search the device info and then display them on searchresult page
    # if not exist, just stay on the same page

    def get(self, request):
        form = DeviceNameForm(request.GET)

        if form.is_valid():
            deviceinfo = form.cleaned_data['deviceinfo']
            results = SkyDevice.search_by_name(deviceinfo)

            if not results:
                    return HttpResponse('<h2>No device as this name is found!</h2>')
            return render(request, "widget/searchresult.html",
                          {'found_device': results,
                           'device_name': deviceinfo})
        else:
            return HttpResponseRedirect(reverse('widget:dashboard'))


class Dashboard(View):
    "main dashboard view"

    def get(self, request):
        return render(request, 'widget/main.html')


class IDGenerator(View):

    # search widget id if it exists and just display on alert page
    # if not exists, generate new 8-digit widget id and then display the result on alert page
    
    def get(self, request):

        device_id = request.GET.get('deviceinfo')
        generator = IDReference.objects.filter(device_id=device_id)

        if generator:
            return render(request, "widget/alert.html", {'WID':generator[0].widget_id})
        else:
            widget_id_generator = IDReference(device_id)
            widget_id_generator.save()
            obj = IDReference.objects.get(device_id=device_id)
            return render(request, "widget/alert.html", {'WID':obj.widget_id})
