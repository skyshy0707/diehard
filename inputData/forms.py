from django import forms
'''from django.contrib.auth.forms import UserCreationForm'''
from .models import Input

'''from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div'''

class CustomInputUserCreationForm(forms.ModelForm):

	'''def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(Fieldset(Div('file', css_class="button20")))'''
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['file'].widget.attrs['class'] = 'btn'
	
	
	class Meta:
		model = Input
		fields = ['title', 'email', 'file']
		labels = {'title':'Название генератора:  ', 'email':'E-mail:  ', 'file': ''}
		