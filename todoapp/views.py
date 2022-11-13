from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from todoapp.models import Posts
from todoapp.forms import CreateTodoForm , UpdateTodoForm
from django.contrib.auth.decorators import login_required

def register_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")

    return render(request , "todoapp/user_register.html" , {"form" : form})

@login_required
def posts_list_view(request):
    posts= Posts.objects.all()
    return render(request , "todoapp/list.html" , {'posts': posts})

@login_required
def create_new_todo_view(request):
    form = CreateTodoForm()

    if request.method == 'POST':
        form = CreateTodoForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/list/")

    return render(request , "todoapp/create_todo.html" , {"form" : form})


@login_required
def detail_todo_view(request , id):
    obj = Posts.objects.get(pk = id)
    return render(request , "todoapp/detail_todo.html" , {"obj" : obj})

@login_required
def update_view(request , id):
    obj = Posts.objects.get(pk = id)
    form = UpdateTodoForm(instance=obj)

    if request.method == 'POST':
        form = UpdateTodoForm(request.POST, request.FILES, instance=obj)
        if form .is_valid():
            form.save()
            return redirect(f'/detail/todo/{obj.id}/')

    return render(request , "todoapp/update.html" , {"obj" : obj , 'form':form})


@login_required
def delete_view(request , id):
    obj = Posts.objects.get(pk = id)
    obj.delete()
    return redirect('/list/')

 

# Create your views here.
