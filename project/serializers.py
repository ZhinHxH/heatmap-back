from rest_framework import serializers
from .models import water_meter, water_meter_ubication

# Since here django knows what is the response for a request like the GET, POST, PUT, etc
# And convert a model in data for the manipuling for the querys
class waterSerializer(serializers.ModelSerializer):
    class Meta:
        # Model that we are going to use on this Serializer with the specifications of 
        model = water_meter
        fields = ('id',
                    'start_code',
                    'data_length',
                    'meter_seria',
                    'cumulative_volume',
                    'alarm',
                    'diagnosis',
                    'valve_status',
                    'checksum',
                    'end_code',
                    'created_at')

#With this constructed we gonna go to stablish the viewset, it which will sta
class ubication(serializers.ModelSerializer):
    class Meta:
        model = water_meter_ubication
        fields = ('id', 'longitude', 'latitude', 'meter_serial', 'efectivity')


    def to_representation(self, instance):
        return {
            "longitude": instance.longitude,
            "latitude": instance.latitude,
            "meter_serial": instance.meter_serial,
            "efectivity": instance.efectivity
        }

