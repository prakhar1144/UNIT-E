from django.contrib import admin
from .models import Mess,Event,Routine

# Register your models here.
admin.site.register(Mess)
admin.site.register(Event)
admin.site.register(Routine)