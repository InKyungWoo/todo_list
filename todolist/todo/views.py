from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from datetime import datetime
# Create your views here.

def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    now = datetime.now()
    return render(request, 'todo/todo_list.html',{'todos': todos, 'now':now})

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form': form})

def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_post.html', {'form': form})

def done_list(request): 
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todo/done_list.html', {'dones': dones})

def todo_done(request, pk): 
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')

# 삭제 기능 추가
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    return redirect('todo_list')

# 삭제 리스트 
def deleted_list(request):
    deleted_todos = Todo.objects.filter(complete=True)
    return render(request, 'todo/deleted_list.html', {'deleted_todos': deleted_todos})
