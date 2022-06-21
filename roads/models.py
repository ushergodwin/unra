from django.db import models

# Create your models here.

class Contractor(models.Model):
    
    contractor_id = models.CharField(max_length=10, primary_key=True)
    contractor_name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=14)
    email = models.EmailField(max_length=50)
    
class Region(models.Model):
    region_id = models.CharField(max_length=10, primary_key=True)
    region_name = models.CharField(max_length=50, null=True)
    

class Staff(models.Model):
    staff_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    position = models.ForeignKey(Region, on_delete=models.CASCADE)
    

class Stations(models.Model):
    station_id = models.CharField(max_length=10, primary_key=True)
    station_name = models.CharField(max_length=50)


class Route(models.Model):
    route_id = models.CharField(max_length=10, primary_key=True)
    route_name = models.CharField(max_length=50)
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE)
    

class Road(models.Model):
    road_id = models.CharField(max_length=10, primary_key=True)
    road_name = models.CharField(max_length=50)
    length = models.FloatField()
    construction_date = models.DateField()
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, max_length=50)
    constructor_id = models.ForeignKey(Contractor, on_delete=models.CASCADE, max_length=10)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE, max_length=10)
    road_map = models.TextField()

    class ROAD_STATUS_CHOICES(models.TextChoices):
        P = 'P', ('Pending')
        O = 'O', ('Ongoing')
        C = 'C', ('Complete')
    road_status = models.CharField(max_length = 15, choices = ROAD_STATUS_CHOICES.choices, default = 'Pending')     
    
    
class Maintenance(models.Model):
    
    class MAINTENANCE_TYPE_CHOICES(models.TextChoices):
        R = 'R', ('routine')
        P = 'P', ('periodic')
        E = 'E', ('emergency')
         
    class ACTIVITIES_CHOICES(models.TextChoices):
        CP = 'CP', ('clearing pavements')
        SG = 'SG', ('shoulder grading')
        PP = 'PP', ('pothole patching')
        OV = 'OV', ('overlay')
        SD = 'SD',('surface dressing')
        TS = 'TS', ('traffic signs')
        DRM = 'DRM', ('debris removal')
        ACC = 'ACC', ('accident')
        DRP = 'DRP', ('damage repair')
    
    maintenance_id = models.CharField(max_length=10, primary_key=True)
    road_id = models.ForeignKey(Road, on_delete=models.CASCADE, max_length=10)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, max_length=10)
    contractor_id = models.ForeignKey(Contractor, on_delete=models.CASCADE, max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    maintenance_type = models.CharField(max_length=20, choices=MAINTENANCE_TYPE_CHOICES.choices)
    activities = models.CharField(max_length=20, choices=ACTIVITIES_CHOICES.choices)
    