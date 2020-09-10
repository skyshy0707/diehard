from django.db import models
'''from django import forms'''
'''from django.contrib.auth.models import AbstractUser'''


from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class Input(models.Model):

	id = models.AutoField(primary_key=True)

	title = models.CharField(max_length=35)
	
	email = models.EmailField()
	
	file = models.FileField()
	
	
	
	
	
'''@receiver(pre_save, sender=Input)
def path_to_rawFile(sender, instance, **kwargs):
	instance.file = models.FileField(upload_to= kwargs["path"])'''
	