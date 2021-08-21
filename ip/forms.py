from django.forms import ModelForm

from ip.models import IP, ElectronicEquipment


class IpForm(ModelForm):
    class Meta:
        model = IP
        fields = ['ips_address', 'activated']


class ElectronicEquipmentForm(ModelForm):
    class Meta:
        model = ElectronicEquipment
        fields = '__all__'
