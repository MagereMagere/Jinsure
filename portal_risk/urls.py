from django.urls import path

from . import views

app_name = 'portal_risk'

urlpatterns = [
	path('', views.risk_assessment, name='path_to_risk_portal'),
]