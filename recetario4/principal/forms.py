#encoding:utf-8 
from django.forms import ModelForm
from django import forms
#we have to make reference of our previous classes
from principal.models import Bebida, Receta, Postre, Comentario

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electrónico')
	mensaje = forms.CharField(widget=forms.Textarea)

class BebidaForm(ModelForm):
    class Meta:
        model = Bebida

class RecetaForm(ModelForm):
    class Meta:
        model = Receta

class PostreForm(ModelForm):
    class Meta:
        model = Postre

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
