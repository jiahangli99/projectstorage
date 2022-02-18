from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Project, Status
from .forms import DateForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def assoc_status(request, project_id, status_id):
  Project.objects.get(id=project_id).status.add(status_id)
  return redirect('detail', project_id=project_id)

def projects_index(request):
  projects = Project.objects.all()
  return render(request, 'project/index.html', {'projects': projects})

def project_detail(request, project_id):
  project = Project.objects.get(id=project_id)
  date_form = DateForm()
  status_project_doesnt_have = Status.objects.exclude(id__in = project.status.all().values_list('id'))
  return render(request, 'project/detail.html', {'project': project,
   'date_form': date_form,
   'status': status_project_doesnt_have
   })

def add_date(request, project_id):
    form = DateForm(request.POST)
    if form.is_valid():
        new_date = form.save(commit=False)
        new_date.project_id = project_id
        new_date.save()
    return redirect('detail', project_id=project_id)

class ProjectCreate(CreateView):
  model = Project
  fields = ('__all__')

class ProjectUpdate(UpdateView):
  model = Project
  fields = ('name', 'description', 'link')

class ProjectDelete(DeleteView):
  model = Project
  success_url = '/projects/'

class StatusList(ListView):
  model = Status
  template_name = 'status/index.html'

class StatusDetail(DetailView):
  model = Status
  template_name = 'status/detail.html'

class StatusCreate(CreateView):
  model = Status
  fields = ('name',)

class StatusUpdate(UpdateView):
    model = Status
    fields = ('name',)

class StatusDelete(DeleteView):
    model = Status
    success_url = '/status/'
