from rest_framework import serializers
from .models import SlaveDevice


class GetSlaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = SlaveDevice
        fields = ['slave_id', 'slave_status']

