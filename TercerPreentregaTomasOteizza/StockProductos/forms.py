from django import forms

class NuevoProcesadorForm(forms.Form):
    marca = forms.CharField(max_length = 30, required=True)
    modelo = forms.CharField(max_length = 30, required=True)
    precio = forms.IntegerField(required=True)
    descripcion = forms.CharField(max_length = 200)
    
class NuevoPlacaVideoForm(forms.Form):
    marca = forms.CharField(max_length = 30, required=True)
    modelo = forms.CharField(max_length = 30, required=True)
    precio = forms.IntegerField(required=True)
    descripcion = forms.CharField(max_length = 200)
    
class NuevoTecladoForm(forms.Form):
    marca = forms.CharField(max_length = 30, required=True)
    modelo = forms.CharField(max_length = 30, required=True)
    precio = forms.IntegerField(required=True)
    descripcion = forms.CharField(max_length = 200)
