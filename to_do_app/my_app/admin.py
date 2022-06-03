from django.contrib import admin
from .models import *
# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    list_display = ("TimeStamp","Title","Description","DueDate","Tag","Status")

#registration to the admin site
admin.site.register(ToDo,ToDoAdmin)