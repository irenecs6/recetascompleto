from django import forms
from .models import *

class FiltroIngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'categoria', 'refrigerado']

class IngredientesForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'categoria', 'refrigerado']

class IngredienteRecetasForm(forms.ModelForm):
    class Meta:
        model = IngredienteRecetas
        fields = ['ingrediente', 'cantidad', 'unidad']