# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
import os,sys,psycopg2.extras

# Create your views here.

def inicial(request):
	titulo = "We need to talk about System Administration"
	proximo = "/slide2/"
        return render_to_response("capa.html",{'titulo': titulo, 'proximo': proximo})

def slide2(request):
	number = 2
	anterior = "/"
	proximo = "/slide3/"
	titulo = "Sysadmin's Twelve"
        return render_to_response("slide2.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide3(request):
	number = 3
	anterior = "/slide2/"
	proximo = "/slide4/"
	titulo = "The Perks of Time Management"
        return render_to_response("slide3.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide4(request):
	number = 4
	anterior = "/slide3/"
	proximo = "/slide5/"
	titulo = "What we got here is a failure in a service"
        return render_to_response("slide4.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide5(request):
	number = 5
	anterior = "/slide4/"
	proximo = "/slide6/"
	titulo = "Elementary, my dear"
        return render_to_response("slide5.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide6(request):
	number = 5
	anterior = "/slide5/"
	proximo = "/slide7/"
	titulo = ""
        return render_to_response("slide6.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})

def slide7(request):
	number = 7
	anterior = "/slide6/"
	proximo = "/slide8/"
	titulo = ""
        return render_to_response("slide7.html",{'titulo': titulo, 'number': number, 'anterior': anterior, 'proximo': proximo})
