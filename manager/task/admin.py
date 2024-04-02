from django.contrib import admin

from task.models import Task, ActionType, Actions

admin.site.register(Task)
admin.site.register(ActionType)
admin.site.register(Actions)