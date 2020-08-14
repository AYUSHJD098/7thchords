from django.shortcuts import render, redirect
from .models import Customer 
from .forms import CustomerForm


def home(request):
	form = CustomerForm()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid(): 
			form.save()
	context = { 'form':form }
	return render(request, 'web/home.html', context)



