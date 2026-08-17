from django.shortcuts import render

def index(request):
    return render(request, 'Projects/index.html')

def activity_1(request):
    return render(request, 'Projects/Activity_1/index.html')