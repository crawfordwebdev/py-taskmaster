from django.contrib import admin
from .models import Task, Penalty, Reward

admin.site.register(Task)
admin.site.register(Penalty)
admin.site.register(Reward)