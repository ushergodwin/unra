from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

class Roads:
    
    def index(self, request):
        return HttpResponseRedirect('unra')


roads_view = Roads()
