from project.models import water_meter, water_meter_ubication
from rest_framework import viewsets, permissions
from .serializers import  *

class water_meter_viewset(viewsets.ModelViewSet):
    queryset = water_meter_ubication.objects.all()
    permission_classes = [permissions.AllowAny]     # With this we can allow that any web can consult the api from any origin
    serializer_class = ubication