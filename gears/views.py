# -*- coding: utf-8 -*-
#from future import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from gears.forms import add_gearForm
from gears.models  import Gear
# Create your views here.

def home(request):
    return render(request, "home.html")#response

#def index(request):
   # return HttpResponse('SpareGear')

def show_gear(request):
    return render (request, "show.html")#response

def add_gear(request):


    if request.method == 'POST':
        Form = add_gearForm(request.POST)
        if Form.is_valid():
            Form.save()
            return HttpResponseRedirect(reverse('gears:show'))

    elif request.method == 'GET':

        form = add_gearForm()

    return render(request, "add_gear.html", {'form': form})

