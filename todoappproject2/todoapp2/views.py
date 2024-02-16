from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import Todotask
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

#class based views
#list view
class LVtask(ListView):
    model = Todotask
    template_name = 'home2.html'
    context_object_name = 'task1'
#detail view
class DVtask(DetailView):
    model = Todotask
    template_name = 'details.html'
    context_object_name ='task1'

#update view
class UVtask(UpdateView):
    model = Todotask
    template_name = 'update.html'
    context_object_name ='task1'
    fields = {'name','priority','date'}
    def get_success_url(self):
         return reverse_lazy('cbid',kwargs={'pk':self.object.id})

#delete view
class DelVtask(DeleteView):
    model = Todotask
    template_name = 'delete.html'
    success_url = reverse_lazy('cbhome')

#function based views
def add(request):
    task1 = Todotask.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date', '')
        task=Todotask(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})
# def details(request):
#     task=Task.objects.all()
#     return render(request,'details.html',{'task':task})

def delete(request,Tid):
    taskid=Todotask.objects.get(id=Tid)
    if request.method=="POST":
        taskid.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,Tid):
    taskid=Todotask.objects.get(id=Tid)
    f=TodoForm(request.POST or None,instance=taskid)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html',{"f":f,"task":taskid})