from django.shortcuts import render, redirect
from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

def index(request):
	return render(request, 'mascotas/index.html', { 'mascotas': Mascota.objects.all() })

def agregar(request):
	if request.method == 'POST':
		mascota_form = MascotaForm(request.POST)
		if mascota_form.is_valid():
			mascota_form.save()
		return redirect('mascotas:index')
	else:
		mascota_form = MascotaForm()
	return render(request, 'mascotas/formulario.html', { 'mascota_form': mascota_form })

def modificar(request, id):
	mascota = Mascota.objects.get(id = id)
	if request.method == 'GET':
		mascota_form = MascotaForm(instance = mascota)
	else:
		mascota_form = MascotaForm(request.POST, instance = mascota)
		if mascota_form.is_valid():
			mascota_form.save()
			return redirect('mascotas:index')
	return render(request, 'mascotas/formulario.html', { 'mascota_form': mascota_form })

def eliminar(request, id):
	mascota = Mascota.objects.get(id = id)
	if request.method == 'POST':
		mascota.delete()
		return redirect('mascotas:index')
	return render(request, 'mascotas/index.html', { 'mensaje_error': 'No se pudo eliminar la Mascota ' + mascota.nombre })
