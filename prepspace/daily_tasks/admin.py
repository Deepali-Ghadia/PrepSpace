from django.contrib import admin
from .models import DailyToDo, Task

# Register your models here.
admin.site.register(DailyToDo)
admin.site.register(Task)