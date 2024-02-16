from django.db import models

# Create the model for the generation of the structure of table of DB
# For this case we can expressive the diferent data types like : CharField, TextField, IntegerField, BooleanField, DateTimeField, FloatField

class water_meter(models.Model):  # class name should be singular, not plural (watter_meter) and in those we define the columns for the project
    start_code = models.CharField(max_length=2)   # Code to initial
    data_length = models.CharField(max_length=2, blank=True)  # Length of data field
    meter_serial = models.CharField(max_length=12, default='varchar')   # Number to identify the meter
    cumulative_volume = models.CharField(max_length = 8, blank = True)   # Is the representative data  is cumulative volume in m3
    alarm = models.CharField(max_length=6, blank=True)   # Alarm description if exist
    diagnosis = models.CharField(max_length=6, blank=True)  # Describe the diferents error types or normal state of the meter
    valve_status = models.CharField(max_length=2, blank=True)   # Valve status for  offline, open or close
    checksum = models.CharField(max_length=4, blank=True)     # Check sum of all bits before it
    end_code  = models.CharField(max_length=2)   # Code to finish
    created_at = models.DateTimeField(auto_now_add = True)   # Date for creation

# We define the new class for mapping the another meters that are registering in the 67 bits model
class watter_meter_old(water_meter):
    hourly_frozen_data = models.CharField(max_length=50, blank = True) # Data frozen each 24 hours
    valve_opening = models.BooleanField()   # Is the state of the valve relationated if is open or close
    voltage_sampling_value =  models.FloatField(blank = True)   # Voltage value sampling
    reserve = models.CharField(max_length=2, blank = True)   # Is necessary more documentation

# we define a  model for the realtion with the ubication of the meters
class water_meter_ubication(models.Model):
    longitude = models.FloatField(max_length=10)   # Longitude of location
    latitude = models.FloatField(max_length=10)   # Latitude of location
    meter_serial = models.CharField(max_length=12)   # Meter serial number for foreing key with other models
    efectivity = models.IntegerField(max_length=3)   # Indicate the effectiveness of installation (%)