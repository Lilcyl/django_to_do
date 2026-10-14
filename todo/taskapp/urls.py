from django.urls import path
from . import views


urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('complete/<int:pk>/', views.CompleteTaskView.as_view(), name='complete_task'),
    path('delete/<int:pk>/', views.DeleteTaskView.as_view(), name='delete_task')
]
# urlpatterns = [
#     path('',views.task_list,name='task_list'),
#     path('complete/<int:pk>/',views.complete_task,name = 'complete_task'),
#     path('delete/<int:pk>/',views.delete_task,name='delete_task')
# ]