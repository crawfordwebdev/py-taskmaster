from django.shortcuts import render


# Add the Cat class & list and view function below the imports
class Task:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

tasks = [
  Task('Lolo', 'tabby', 'Kinda rude.', 3),
  Task('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Task('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Task('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def tasks_index(request):
  return render(request, 'tasks/index.html', { 'tasks': tasks })