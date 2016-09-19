from django.shortcuts import render
from .models import Secret

def index(request):
	context = {
		"secrets" = Secret.objects.all()
	}
	return render(request, 'secrets/index.html', context)

def secrets(request):
	Secret.objects.create(description=request.POST['description'])
	return redirect('/')