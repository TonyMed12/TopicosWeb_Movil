import uuid
from datetime import timedelta

from django.shortcuts import get_object_or_404

from .models import Pedido
from .medios import crear_medio
from .sugerencias import (
    AdaptadorJSON, AdaptadorXML, proveedor_json_falso, proveedor_xml_falso,
)


def registrar_pedido(destino, proveedor='json'):
    proveedores = {
        'json': (proveedor_json_falso, AdaptadorJSON()),
        'xml': (proveedor_xml_falso, AdaptadorXML()),
    }
    try:
        consultar, adaptador = proveedores[proveedor]
    except KeyError as error:
        raise ValueError(f'Proveedor desconocido: {proveedor}') from error

    sugerencia = adaptador.traducir(consultar(destino))
    medio = crear_medio(sugerencia.medio)
    folio = f"PED-{uuid.uuid4().hex[:8].upper()}"
    pedido = Pedido(folio=folio, destino=destino)
    plan = medio.planear(pedido, {'motivo': sugerencia.motivo})
    pedido.medio = plan.medio
    pedido.detalle_plan = plan.detalle
    pedido.horas_estimadas = plan.horas_estimadas
    pedido.save()
    return pedido


def obtener_seguimiento(pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return {
        'folio': pedido.folio,
        'estado': pedido.get_estado_display(),
        'eta': pedido.creado_en + timedelta(hours=pedido.horas_estimadas),
        'medio': pedido.medio,
        'detalle_plan': pedido.detalle_plan,
    }
