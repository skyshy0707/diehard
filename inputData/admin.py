from django.contrib import admin

from .models import Input
from .forms import CustomInputUserCreationForm

# Register your models here.


admin.site.register(Input)


