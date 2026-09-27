from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from . import services


@require_POST
def crear_pedido(request):
    pedido = services.registrar_pedido(destino=request.POST.get('destino', ''))
    return redirect('detalle_pedido', pedido_id=pedido.id)


def detalle_pedido(request, pedido_id):
    contexto = services.obtener_seguimiento(pedido_id)
    return render(request, 'entregas/seguimiento.html', contexto)
