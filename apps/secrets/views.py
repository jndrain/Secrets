from django.shortcuts import render
from .models import Secret

def index(request):
	return render(request, 'secrets/index.html')

def secrets(request):
	Secret.objects.create(description=request.POST['description'])