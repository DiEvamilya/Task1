"""
URL configuration for manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from task.views import TasklistView, TaskDetailView, TaskUpdateView, TaskCreateView, TaskDeleteView, HistoryListView, \
    View, CompletedView, action_history_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TasklistView.as_view(), name='list_task'),
    path('detail/<slug:task_slug>/', TaskDetailView.as_view(), name='task_detail'),
    path('update/<int:task_pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<slug:slug>/delete/', TaskDeleteView.as_view(), name='task_delete'), # Испр��влено
    path('history/', HistoryListView.as_view(), name='history'),
    path('completed/<int:task_pk>/', CompletedView.as_view(), name='completed'),
    path('action_history/', action_history_view, name='action_history')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

