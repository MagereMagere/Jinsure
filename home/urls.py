from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
	path('', views.home_page, name='path_to_home'),
	path('contact/', views.contact_page, name='path_to_contact'),
]