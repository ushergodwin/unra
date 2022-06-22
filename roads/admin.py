from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django import forms
from django.utils.html import format_html

from roads.models import (
    Contractor, 
    Maintenance, 
    Region, 
    Road, 
    Route, 
    Staff, 
    Stations
)

# Register your models here.

class unraAdmin(admin.AdminSite):
    site_header = "UNRA ADMINISTRATION"
    site_title = "ADMIN"
    index_title= "UNRA"

class ContractorAdmin(admin.ModelAdmin):
    list_display = ('contractor_name','telephone', 'email', 'contractor_id')
    list_display_links = ('contractor_name',)
    search_fields = ['contractor_name', 'telephone', 'contractor_id']
    

class RegionAdmin(admin.ModelAdmin):
    list_display = ('', ) 
    
    
class RegionChoicesField(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return f"{obj.region_name}"
    
class StationChoicesField(forms.ModelChoiceField):
    
    def label_from_instance(self, obj):
        return f"{obj.station_name}"
    
    
class ContractorChoicesField(forms.ModelChoiceField):
    
    def label_from_instance(self, obj):
        return f"{obj.contractor_name}"

class RouteChoicesField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.route_name}"
  
    
class StaffChoicesField(forms.ModelChoiceField):
    
    def label_from_instance(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class RoadChoicesField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.road_name}"
  
    
class RoutesAdmin(admin.ModelAdmin):
    
    list_display = ('route_id', 'route_name', 'region')
        
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'region_id':
            return RegionChoicesField(queryset=Region.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)  
    
    def region(self, obj):
        return obj.region_id.region_name


class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_id', 'region_name')
    list_display_links = ('region_name', )
    

class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'first_name', 'last_name', 'region_name', 'station_name')
    list_display_links = ('first_name', 'staff_id')
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'region_id':
            return RegionChoicesField(queryset=Region.objects.all())
        elif db_field.name == 'station_id':
            return StationChoicesField(queryset=Stations.objects.all())
        
        return super().formfield_for_foreignkey(db_field, request, **kwargs) 
    
    def region_name(self, obj):
        return "N/A" if obj.region is None else obj.region.region_name 
    
    def station_name(self, obj):
        return "N/A" if obj.station_id is None else obj.station_id.station_name


class StationAdmin(admin.ModelAdmin):
    list_display = ('station_name', 'station_id')
    list_display_links = ('station_name', 'station_id')
    

class RoadAdmin(admin.ModelAdmin):
    list_display = (
        'road_name', 'length', 'route', 'contractor', 
        'construction_date', 'road_on_map'
        )
    
    list_display_links = ('road_name',)
    
    list_filter = ['length', 'route_id', 'constructor_id']
    
    search_fields = ['road_name', 'length', 'constructor_id']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'constructor_id':
            return ContractorChoicesField(queryset=Contractor.objects.all())
        elif db_field.name == 'route_id':
            return RouteChoicesField(queryset=Route.objects.all())
        elif db_field.name == 'staff_id':
            return StaffChoicesField(queryset=Staff.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs) 
    
    def route(self, obj):
        return obj.route_id.route_name
    
    def contractor(self, obj):
        return obj.constructor_id.contractor_name
    
    def road_on_map(self, obj):
        return format_html("<a href='javascript:void(0)' onClick=\"window.open('{}','gotFusion','toolbar=1,location=1,directories=0,status=0,menubar=1,scrollbars=1,resizable=1,copyhistory=0,width=800,height=600,left=0,top=0')\"> {} </a>", obj.road_map, 'View on Map')
    
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = (
        'maintenance_id', 'end_date', 'road', 'start_date', 
        'staff', 'contractor', 'maintenance_type', 'activities'
        ) 
    
    list_display_links = ('maintenance_id',)
    list_filter = ['start_date', 'end_date', 'contractor_id']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'contractor_id':
            return ContractorChoicesField(queryset=Contractor.objects.all())
        elif db_field.name == 'road_id':
            return RoadChoicesField(queryset=Road.objects.all())
        elif db_field.name == 'staff_id':
            return StaffChoicesField(queryset=Staff.objects.all())
        return super().formfield_for_foreignkey(db_field, request, **kwargs) 
    
    def road(self, obj):
        return obj.road_id.road_name
    
    def staff(self, obj):
        return f"{obj.staff_id.first_name} {obj.staff_id.last_name}"
    
    def contractor(self, obj):
        return f"{obj.contractor_id.contractor_name}".upper()


unra_admin = unraAdmin(name="unra")
unra_admin.register(Group, GroupAdmin)
unra_admin.register(User, UserAdmin)
unra_admin.register(Contractor, ContractorAdmin)
unra_admin.register(Region, RegionAdmin)
unra_admin.register(Staff, StaffAdmin)
unra_admin.register(Stations, StationAdmin)
unra_admin.register(Route, RoutesAdmin)
unra_admin.register(Road, RoadAdmin)
unra_admin.register(Maintenance)
