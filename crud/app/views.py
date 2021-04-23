from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.

def showMsg(request):
    data=Todo.objects.all()
    data2='This is my Msg...'
    context = {
        'data':data,
        'data2':data2
    }
    return render(request,"main.html",context)

def details_view(request,id):
    data=Todo.objects.get(id=id)
    context = {
        'data':data
    }
    return render(request,"details.html",context)

def create_view(request):
    form=TodoForm(request.POST or None)
    data='This is for create'
    if form.is_valid():
        form.save()
        return redirect("/MyMessage/")

    context = {
        'form':form,
        'data':data
    }
    return render(request,"create.html",context)


def update_view(request,id):
    data=Todo.objects.get(id=id)
    form = TodoForm(request.POST or None,instance=data)

    if form.is_valid():
        form.save()
        return redirect("/MyMessage/")

    context={
        "form":form
    }

    return render(request,"update.html",context)

def delete_task(request,id):
    data=Todo.objects.get(id=id)
    data.delete()
    return redirect("/MyMessage/")


