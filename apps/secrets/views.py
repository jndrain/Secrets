from django.shortcuts import render, redirect
from .models import Secret

def index(request):
	context = {
		"secrets": Secret.objects.all()
	}
	return render(request, 'secrets/index.html', context)

def create_secret(request):
	Secret.objects.create(secret=request.POST['secret'])
	return redirect('/')
