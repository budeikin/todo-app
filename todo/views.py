from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from todo.models import Task
from todo.forms import TaskUpdateForm


class TodoListView(ListView):
    model = Task
    template_name = 'todo/todo_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class CreateTaskView(CreateView):
    model = Task
    fields = ['title']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTaskView, self).form_valid(form)


class DeleteTaskView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = '/'


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = '/'
    template_name = 'todo/update_task.html'


class CompleteView(View):
    model = Task
    success_url = reverse_lazy('task-list')

    def get(self, *args, **kwargs):
        i_object = Task.objects.get(id=kwargs.get('pk'))
        i_object.is_completed = True
        i_object.save()
        return redirect(self.success_url)


class BackCompleteView(View):
    model = Task
    success_url = reverse_lazy('task-list')

    def get(self, *args, **kwargs):
        i_object = Task.objects.get(id=kwargs.get('pk'))
        i_object.is_completed = False
        i_object.save()
        return redirect(self.success_url)


