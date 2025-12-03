from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('relaciones', views.relaciones, name='relaciones'),

    path('recetas', views.recetas_lista, name='recetas_lista'),
    path('receta/<int:pk>', views.receta_detalle, name='receta_detalle'),
    path('receta/<int:receta_pk>/agregar_ingrediente/<int:ingrediente_pk>', views.receta_agregar_ingrediente, name='receta_agregar_ingrediente'),

    path('ingredientes', views.ingredientes_lista, name='ingredientes_lista'),
    path('ingredientes/nuevo', views.ingredientes_nuevo, name='ingredientes_nuevo'),
    path('ingredientes/nuevomodel', views.ingredientes_nuevo_model, name='ingredientes_nuevo_model'),
]