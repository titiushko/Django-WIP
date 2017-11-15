from django.shortcuts import render, redirect
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

def index(request):
	return render(request, 'inicio.html')

def agregar(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:inicio')
	else:
		form = MascotaForm()
	return render(request, 'mascota/agregar.html', { 'nueva_mascota': form })
