from django import forms

class DeviceNameForm(forms.Form):
    deviceinfo = forms.CharField()
