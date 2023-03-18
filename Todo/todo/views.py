from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm
# Create your views here.

def index(request):

    if request.method == 'POST':
        text= request.POST['text']
        print(text)
        new_todo = Todo(text=text)
        new_todo.save()
        return redirect(index)

    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    context = {'todo_list':todo_list, 'form':form}

    return render(request, 'index.html', context)

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect(index)

def deletecompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect(index)

def deletall(request):
    Todo.objects.all().delete()
    return redirect(index)