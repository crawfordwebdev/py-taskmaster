from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Task

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tasks_index(request):
  tasks = Task.objects.filter(user=request.user)
  # Can also retrieve the logged in user's tasks like this
  # tasks = request.user.task_set.all()
  return render(request, 'tasks/index.html', { 'tasks': tasks })

def tasks_detail(request, task_id):
  task = Task.objects.get(id=task_id)
  return render(request, 'tasks/detail.html', { 'task': task })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('tasks_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})

class TaskCreate(CreateView):
  model = Task
  fields = '__all__'
  success_url = '/tasks/'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the task
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class TaskUpdate(UpdateView):
  model = Task
  fields = '__all__'

class TaskDelete(DeleteView):
  model = Task
  success_url = '/tasks/'

class Home(LoginView):
  template_name = 'home.html'