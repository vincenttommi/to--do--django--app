from django.contrib import admin

#registering models here
from .models import Todo

admin.site.register(Todo)

