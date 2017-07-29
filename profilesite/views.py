from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import DetailView, TemplateView

def index(request, template="index.html"):
	return (request, template)
