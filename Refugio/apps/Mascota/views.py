from django.shortcuts import render, redirect
from django.http import JsonResponse
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
	if request.method == 'GET':
		mascota.delete()
		return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Mascota ' + mascota.nombre})
	return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Mascota ' + mascota.nombre})
