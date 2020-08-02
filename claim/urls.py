from django.urls import path

from . import views

app_name = 'claim'

urlpatterns = [
	path('', views.add_claim, name='path_to_claim')
]