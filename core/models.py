from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='productos')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['created']

    def __str__(self):
        return self.name