from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
	return render_to_response(
		'home.html', {}, context_instance=RequestContext(request))

def schedule(request):
	return render_to_response(
		'schedule.html', {}, context_instance=RequestContext(request))

def accommodation(request):
	return render_to_response(
		'accommodation.html', {}, context_instance=RequestContext(request))

def transportation(request):
	return render_to_response(
		'transportation.html', {}, context_instance=RequestContext(request))

def lectures(request):
	return render_to_response(
		'lectures.html', {}, context_instance=RequestContext(request))

def download(request):
	return render_to_response(
		'download.html', {}, context_instance=RequestContext(request))

def contact_us(request):
	return render_to_response(
		'contact_us.html', {}, context_instance=RequestContext(request))

def registration(request):
	return render_to_response(
		'registration.html', {}, context_instance=RequestContext(request))

