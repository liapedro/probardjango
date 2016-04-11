from django.shortcuts import render
from .forms import RegForm
from .models import Registrado
# Create your views here.


def inicio(request):
	form = RegForm(request.POST or None)
	context = {
		"form":form
	}
	if form.is_valid():
		#print form.cleaned_data
		#form_dicc = form.cleaned_data
		#print form_dicc.get("nombre")
		form_data = form.cleaned_data
		abc = form_data.get("nombre_form")
		obj = Registrado.objects.create(nombre = abc)

		#obj2 = Registrado() 
		#obj2.nombre = abc
		#obj2.save()
		


	return render(request, "inicio.html", context)