from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
#    url(r'^$', views.index),
	 url(r'^$', TemplateView.as_view(template_name='home_page.html')),
]