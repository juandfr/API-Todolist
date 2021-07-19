from django.urls import path, include

from task import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('tasks/usuario/<int:fk>/', views.TaskFilter.as_view()),
]