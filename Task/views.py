from django.shortcuts import render

# Create your views here.
tasks = ["Go shopping", "Go cycling", "Visit children's home","Deliver fruits"]
def task(request):
    return render(request, "task.html",{
        "tasks": tasks
    })

def add(request):
    return render(request, "add.html")