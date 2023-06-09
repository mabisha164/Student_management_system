from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import student
# Create your views here.
def index(request):
  return render(request,'students/index.html',{
        'students':student.objects.all()
    }) 

def view_student(request, id):
  students = student.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))