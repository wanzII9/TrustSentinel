from django.contrib import admin
from django.contrib.auth.models import Group
from .models import PLCList, SlaveDevice

# Register your models here.
admin.site.unregister(Group)

@admin.register(PLCList)
class PLCListAdmin(admin.ModelAdmin):
    list_display = ('plc_id',)
    list_display_links = ('plc_id',)


@admin.register(SlaveDevice)
class SlaveDeviceAdmin(admin.ModelAdmin):
    list_display = ('plc_id', 'slave_id', 'slave_vendor', 'slave_product', 'slave_version', 'product_id', 'slave_temp')
    list_display_links = ('slave_id',)

