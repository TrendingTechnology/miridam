from django.forms import ModelForm

from ip.models import IPv4


class Ipv4Form(ModelForm):
    class Meta:
        model = IPv4
        fields = ['ipv4_address', 'department', 'activated']
