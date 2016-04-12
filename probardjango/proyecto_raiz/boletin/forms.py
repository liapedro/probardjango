from django import forms
from .models import Registrado

class RegistradoForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre","email"] #Lista de campos 

	def clean_email(self):
		email = self.cleaned_data.get("email")

		#Dividimos el correo en dos partes, donde el @ queda en medio
		email_base, proveedor = email.split("@")
		#dividimos y sacamos el dominio y la extension del correo a la derecha del @
		dominio, extension = proveedor.split(".")
		#comparamos que la extension tenga terminacion .edu
		if not extension == "edu":
			raise forms.ValidationError("Por favor utilice correo con extension .edu")

		#if not "edu" in email: #Valida que el texto que se ingreso en el campo de email contenta la palabra edu
		#	raise forms.ValidationError("Utilice correo con extencion .edu")

		return email





#Creacion de el formulario de registro
#class RegForm(forms.Form):
#	nombre_form = forms.CharField(max_length = 100) 
#	edad = forms.IntegerField()