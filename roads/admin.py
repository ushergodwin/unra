from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
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
    
    # def __init__(self, *args, **kwargs) -> None:
    #     super(unraAdmin, self).__init__(*args, **kwargs)
    #     self._registry.update(admin.site._registry)
    
unra_admin = unraAdmin(name="unra")
unra_admin.register(Group, GroupAdmin)
unra_admin.register(User, UserAdmin)
unra_admin.register(Contractor)
unra_admin.register(Region)
unra_admin.register(Staff)
unra_admin.register(Stations)
unra_admin.register(Route)
unra_admin.register(Road)
unra_admin.register(Maintenance)
