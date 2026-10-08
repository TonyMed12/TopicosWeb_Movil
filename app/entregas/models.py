from django.db import models


class Pedido(models.Model):
    ESTADOS = [
        ('registrado', 'Registrado'),
    ]

    folio = models.CharField(max_length=20, unique=True, editable=False)
    destino = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='registrado')
    medio = models.CharField(max_length=20, blank=True, default='')
    detalle_plan = models.CharField(max_length=100, blank=True, default='')
    horas_estimadas = models.PositiveSmallIntegerField(default=2)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.folio
