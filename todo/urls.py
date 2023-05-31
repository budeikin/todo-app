from django.urls import path
from todo import views

urlpatterns = [
    path('list/', views.TodoListView.as_view(), name='task-list'),
    path('add/', views.CreateTaskView.as_view(), name='task-add'),
    path('delete/<int:pk>', views.DeleteTaskView.as_view(), name='task-delete'),
    path('update/<int:pk>', views.UpdateTaskView.as_view(), name='task-update'),
    path('complete/<int:pk>', views.CompleteView.as_view(), name='task-complete'),
    path('uncomplete/<int:pk>', views.BackCompleteView.as_view(), name='task-uncomplete'),
]

