from django.contrib import admin
from ip.models import IPv4


@admin.register(IPv4)
class IPv4Admin(admin.ModelAdmin):
    list_display = ['id', 'ipv4_address']
    list_display_links = ['id', 'ipv4_address']
