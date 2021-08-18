from django.forms import ModelForm

from ip.models import IP


class Ipv4Form(ModelForm):
    class Meta:
        model = IP
        fields = ['ips_address', 'department', 'activated']
