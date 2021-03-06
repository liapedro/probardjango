from django.shortcuts import render
from .forms import RegistradoForm
from .models import Registrado
# Create your views here.


def inicio(request):
	titulo = "Bienvenidos"
	form = RegistradoForm(request.POST or None, request.FILES or None) #Mostramos y validamos el formulario que tenemos en form.py
	
	#Creamos variable para nuestra consulta query
	queryset = Registrado.objects.all()
	#Creamos bucle para leer los objetos que arroja la consulta
	for obj in queryset:
		print obj.id
		print obj.nombre
		print obj.email
		print obj.media

	contexto = {
		"titulo": titulo,
		"form": form,
		"queryset": queryset,
	}


	if form.is_valid():
		instance = form.save(commit = False) #No guarda la informacio en la base de datos
		nombre = form.cleaned_data.get("nombre") #Pedimos el nombre del formulario
		email = form. cleaned_data.get("email")
		form.save()

		contexto = {
			"titulo":"Gracias %s, ya se ha registrado." %(nombre)
		}

		if not nombre:
			contexto = {
				"titulo":"Gracias %s, ya se ha registrado." %(email)
			}
		#print instance

	###############################################

	# Valida que el usuario este loggeado para que aparezca un mensaje
	# de bienvenida personalizado con su nombre

	# if request.user.is_authenticated():
	# 	titulo = "Hola, %s!" %(request.user)

	###############################################

	
		


	return render(request, "inicio.html", contexto)	

def sobre(request):
	titulo = "Sobre Nosotros"
	
	contexto = {
		"titulo": titulo,
	}



	return render(request, "sobre.html", contexto)	