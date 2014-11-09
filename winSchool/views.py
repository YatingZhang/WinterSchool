from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
	return render_to_response(
		'home.html', {}, context_instance=RequestContext(request))

def schedule(request):
	return render_to_response(
		'schedule.html', {}, context_instance=RequestContext(request))

def hotel(request):
	return render_to_response(
		'hotel.html', {}, context_instance=RequestContext(request))

def transport(request):
	return render_to_response(
		'transport.html', {}, context_instance=RequestContext(request))

def professor(request):
	return render_to_response(
		'professor.html', {}, context_instance=RequestContext(request))

def download(request):
	return render_to_response(
		'download.html', {}, context_instance=RequestContext(request))

def about(request):
	return render_to_response(
		'about.html', {}, context_instance=RequestContext(request))



