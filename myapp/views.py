from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_list_or_404

# Create your views here.
def index (request):
    return HttpResponse("Index page")

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return HttpResponse("About")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = get_list_or_404(Task, id=id)
    return HttpResponse('task: %s' % task.title)

def tasksByName(request, title):
    task = Task.objects.get(title = title)
    return HttpResponse('task: %s' % task.title)