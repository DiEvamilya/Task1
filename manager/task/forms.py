from django import forms
from django.forms import DateTimeInput, DateInput

from task.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = 'slug',
        widgets = {
            'deadline': DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'completed_at': DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            # Определяем виджет для поля deadline
        }

        # Этот метод необходим для правильной работы формата даты-времени в HTML5
        def __init__(self, *args, **kwargs):
            super(TaskForm, self).__init__(*args, **kwargs)
            self.fields['deadline'].input_formats = ('%Y-%m-%dT%H:%M',)
            self.fields['completed_at'].input_formats = ('%Y-%m-%dT%H:%M',)