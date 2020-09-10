from django.db import models
from django import forms

from inputData.models import Input

from django.contrib.postgres.fields import JSONField

# Create your models here.

class Results(models.Model):

	'''form = uform(request.POST, request.FILES)'''
	
	generator = models.OneToOneField(Input, on_delete = models.CASCADE, primary_key = True)
	
	'''path = models.FilePathField()'''
	
	pvalues = JSONField()
	
	
	
	
	
	'''if form.is_valid():
		filename = request.FILES['file'].name

		generator = models.OneToOneField(Input, on_delete = models.CASCADE, primary_key = True)
	
		id_generator = generator.id
	
		path = id_generator + '/' + filename'''