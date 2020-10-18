


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Screening, Viewer, Friend, Genre, Ticket

# Create your views here.

def index(request):
	things = Screening.objects
	template = loader.get_template('movies/index.html')
	context = {'things':things}
	return HttpResponse(template.render(context, request))

def movies(request):
	return render(request, 'movies/movies.html')