from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from .models import Task
from .forms import TaskForm

class TaskListView(View):
    template_name = "taskapp/task_list.html"

    def get(self, request):
        form = TaskForm()
        tasks = Task.objects.order_by('-created_at')

        return render(request, self.template_name, {'form': form, 'tasks': tasks})

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('task_list')

        tasks = Task.objects.order_by('-created_at')

        return render(request, self.template_name, {'form': form, 'tasks': tasks})
        

class CompleteTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.completed = True
        task.save()
        return redirect('task_list')

class DeleteTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_list')

    

# from django.shortcuts import render,redirect,get_object_or_404
# from .models import Task
# from .forms import TaskForm
# # Create your views here.



# def task_list(request):
#     if(request.method ==  "POST"):
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm()
#     tasks = Task._default_manager.order_by('-created_at')
#     return render(request,'taskapp/task_list.html',{'form':form,'tasks':tasks})

# def complete_task(request,pk):
#     if(request.method == "POST"):
#         task = get_object_or_404(Task,pk=pk)
#         task.completed = True
#         task.save()
#     return redirect("task_list")
# def delete_task(request,pk):
#     if(request.method == "POST"):
#         task = get_object_or_404(Task,pk=pk)
#         task.delete()
#     return redirect("task_list")