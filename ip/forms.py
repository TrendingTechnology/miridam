from django.forms import ModelForm

from ip.models import IP


class IpForm(ModelForm):
    class Meta:
        model = IP
        fields = ['ips_address', 'activated']
