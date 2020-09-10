from django.urls import path, re_path

from . import views

'''urlpatterns = [
	path('results/', views.results, name='results'),
	path(r'^results/(?P<pk>[0-9]\d+)', views.result , name = 'result'),
]'''

app_name = 'results'

urlpatterns = [
	re_path(r'^results/$', views.results, name='results'),
	re_path(r'^results/(?P<res_id>[0-9]+)/$', views.result , name = 'result'),
]