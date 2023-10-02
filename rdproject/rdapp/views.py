from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def projects(request):
    return render(request,'projects.html')
def index(request):
    return render(request,'index.html')
def skills(request):
    return render(request,'skills.html')
def exp(request):
    return render(request,'education&exp.html')
