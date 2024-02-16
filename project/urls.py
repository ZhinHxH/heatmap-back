# This file is for create the routes of the application manually
from rest_framework import routers
from .api import water_meter_viewset

router = routers.DefaultRouter()   # This is that found for create the crud

router.register('api/project', water_meter_viewset, 'project')   # With this we specificate the routes for register with the api relation

# Once create the route, we need to create an urlpatterns, genering the four basis method like the GET for general
# POST for create a new elements, PUT/PATCH for actualize and DELETE to delete an element

urlpatterns = router.urls


