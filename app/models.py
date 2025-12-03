from django.db import models

# Create your models here.

# class CategoriaChoices(models.TextChoices):
#     LEGUMBRE = "LE", "Legumbres"

class UnidadChoices(models.TextChoices):
    GRAMOS = "G",
    KILOGRAMOS = "KG",
    LITRO = "L",
    UNIDADES = "U"
        
class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.ManyToManyField('Ingrediente', through="IngredienteRecetas")

    def __str__(self) -> str:
        return f"{self.nombre}"

class CategoriaIngrediente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre}"

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaIngrediente, on_delete=models.CASCADE)
    refrigerado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.categoria})"
    
class IngredienteRecetas(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, unique=True)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, unique=True)
    cantidad = models.FloatField()
    unidad = models.CharField(max_length=2, choices=UnidadChoices.choices)
    
    class Meta:
        unique_together = ('receta', 'ingrediente')
        
    def __str__(self):
        return f"{self.receta} - {self.cantidad} {self.unidad} de {self.ingrediente}"