import uuid
from datetime import timedelta

from django.shortcuts import get_object_or_404

from .models import Pedido


def registrar_pedido(destino):
    folio = f"PED-{uuid.uuid4().hex[:8].upper()}"
    return Pedido.objects.create(folio=folio, destino=destino)


def obtener_seguimiento(pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return {
        'folio': pedido.folio,
        'estado': pedido.get_estado_display(),
        'eta': pedido.creado_en + timedelta(hours=2),
    }
