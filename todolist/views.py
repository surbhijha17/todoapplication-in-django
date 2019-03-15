from django.shortcuts import render
from .forms import *
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse ,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
User=get_user_model()

from django.contrib.auth.decorators import login_required
@login_required
def home(request):

    list=Todo.objects.all().order_by('-id').filter(user=request.user)
    form = TodoForm()


    if request.method=="POST":
        form=TodoForm(request.POST or None)
        if form.is_valid():
            u=form.save(commit=False)
            u.user=request.user
            print(u.user)

            u.save()
            form=TodoForm()
    todos=Todo.objects.all().filter(mark__exact=True).filter(user=request.user)
    now=datetime.datetime.now().strftime('%H:%M')
    print(now)
    for todo in list:
        l=(todo.time.strftime('%H:%M'))
        print(l)
        content=str(todo.content)
        u=str(todo.user.email)
        if now==l:
            send_mail('todo mail',content,'surbhijha1717@gmail.com',[u])

    return render(request,'todolist/index.html',{'list':list,'form':form,'todos':todos})
@login_required
def see(request,pk):
    list=Todo.objects.filter(pk=pk)

    return render(request,'todolist/schedule.html',{'list':list})
@login_required
def mark(request,pk):
    todo=Todo.objects.get(pk=pk)
    todo.mark=True
    todo.save()
    return redirect('todolist:home')
@login_required
def unmark(request,pk):
    todo=Todo.objects.get(pk=pk)
    todo.mark=False
    todo.save()
    return redirect('todolist:home')
@login_required
def deletecompleted(request):
    Todo.objects.filter(mark__exact=True).delete()

    return redirect('todolist:home')
@login_required
def delete(request,pk):

    todo=Todo.objects.get(pk=pk)
    todo.delete()

    return redirect('todolist:home')
@login_required
def update(request,pk):
    todo=get_object_or_404(Todo,pk=pk)
    form = TodoForm()
    if request.method=="POST":
        form=TodoForm(request.POST or None,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todolist:home')
    return render(request,'todolist/update.html',{'form':form})
