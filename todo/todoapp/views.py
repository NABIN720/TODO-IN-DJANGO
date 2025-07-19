from django.shortcuts import render,redirect
from httpx import delete
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/index.html',{'todos':todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title'] #.get ni use garda hunxa title=request.POST.get('title') yestai yeastai
        Todo.objects.create(title=title)
        return redirect('index')
    return render(request, 'todoapp/add.html')

def complete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = True
    # todo.save()
    todo.delete()  #todo.save is boring why to show completed todos
    return redirect('index')
