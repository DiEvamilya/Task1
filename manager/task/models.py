from django.db import models

from django.utils.text import slugify




class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=10, choices=[('v', 'высокий'), ('s', 'средний'), ('n', "низкий")])
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('в процессе', 'pr' ), ('com', 'закончен')], default='в процессе')
    completed_at = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    slug = models.SlugField(max_length=20, null=True, blank=True, unique=True)


    def __str__(self):
        return self.title


    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.title} - {self.id}')
        return super().save()

class ActionType(models.Model):
    action_name = models.CharField(max_length=255)


class Actions(models.Model):
    action = models.ForeignKey(ActionType, on_delete=models.CASCADE)
    made_ad = models.DateTimeField(blank=True, null=True)


