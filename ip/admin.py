from django.contrib import admin
from ip.models import IP


@admin.register(IP)
class IPv4Admin(admin.ModelAdmin):
    list_display = ['id', 'ips_address']
    list_display_links = ['id', 'ips_address']
