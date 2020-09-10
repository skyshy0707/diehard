from django.urls import path

from . import views

app_name = 'inputData'

urlpatterns = [
	path('', views.upload_file, name='home'),
]