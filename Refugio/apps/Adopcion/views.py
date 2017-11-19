from django.http import Http404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from apps.adopcion.forms import PersonaForm
from apps.adopcion.models import Persona

class index(ListView):
    model = Persona
    template_name = 'adopciones/index.html'

class agregar(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'adopciones/formulario.html'
    success_url = reverse_lazy('adopciones:index')

class modificar(UpdateView):
	model = Persona
	form_class = PersonaForm
	template_name = 'adopciones/formulario.html'
	success_url = reverse_lazy('adopciones:index')

def eliminar(request, id):
	if not request.is_ajax():
		raise Http404("Error: Solicitud denegada - Esta acción solo se puede ejecutar desde una llamada Ajax.")
	persona = Persona.objects.get(id = id)
	if request.method == 'GET':
		persona.delete()
		return JsonResponse({'error': False, 'mensaje': 'Se eliminó la Persona ' + persona.nombres})
	return JsonResponse({'error': True, 'mensaje': 'No se pudo eliminar la Persona ' + persona.nombres})
