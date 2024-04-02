from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View

from task.forms import TaskForm
from task.models import Task


class TasklistView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    # def get_context_data(self, *, object_list=None, **kwargs):



class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
    slug_url_kwarg = 'task_slug'



class TaskCreateView(CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('list_task')


class TaskUpdateView(UpdateView):
    template_name = 'task_update.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('list_task')
    pk_url_kwarg = 'task_pk'



class TaskDeleteView(DeleteView):
    template_name = 'task_delete.html'
    model = Task
    success_url = reverse_lazy('list_task')


class HistoryListView(ListView):
    model = Task
    template_name = 'history.html'
    context_object_name = 'task'
    queryset = Task.objects.all().order_by("-created_at")


class CompletedView(View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs.get('task_pk'))

        # Помечаем задачу как выполненную
        task.completed = True
        task.save()

        # Переносим задачу на страницу History
        task.status = True
        task.save('history.html')

        # Перенаправляем на страницу History
        return redirect(reverse('history'))

        tas

def action_history_view(reguest):
    task = Task.objects.all()
    context = {'task': task}
    return render(reguest, 'action_history.html', context)


