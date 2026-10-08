from django.test import TestCase

from .models import Pedido
from .medios import crear_medio
from .services import registrar_pedido
from .sugerencias import AdaptadorJSON, AdaptadorXML, Sugerencia


class PedidoTests(TestCase):
    def test_post_crea_pedido_y_redirige_al_seguimiento(self):
        respuesta = self.client.post('/pedidos/', {'destino': 'Calle 1, Ciudad'})
        pedido = Pedido.objects.get()
        self.assertRedirects(respuesta, f'/pedidos/{pedido.id}/')

    def test_seguimiento_muestra_folio_y_estado(self):
        self.client.post('/pedidos/', {'destino': 'Calle 1, Ciudad'})
        pedido = Pedido.objects.get()
        respuesta = self.client.get(f'/pedidos/{pedido.id}/')
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, pedido.folio)
        self.assertContains(respuesta, 'Registrado')

    def test_recargar_no_crea_otro_folio(self):
        self.client.post('/pedidos/', {'destino': 'Calle 1, Ciudad'})
        pedido = Pedido.objects.get()
        self.client.get(f'/pedidos/{pedido.id}/')
        self.client.get(f'/pedidos/{pedido.id}/')
        self.assertEqual(Pedido.objects.count(), 1)

    def test_get_a_pedidos_no_crea_nada(self):
        respuesta = self.client.get('/pedidos/')
        self.assertEqual(respuesta.status_code, 405)
        self.assertEqual(Pedido.objects.count(), 0)

    def test_pedido_inexistente_da_404(self):
        respuesta = self.client.get('/pedidos/999/')
        self.assertEqual(respuesta.status_code, 404)

    def test_json_y_xml_se_traducen_al_mismo_contrato(self):
        self.assertEqual(
            AdaptadorJSON().traducir('{"route_hint":"dron","score":0.9}').medio,
            'dron',
        )
        self.assertEqual(
            AdaptadorXML().traducir('<recommendation><vehicle>dron</vehicle></recommendation>').medio,
            'dron',
        )
        self.assertIsInstance(AdaptadorJSON().traducir('{"route_hint":"dron","score":0.9}'), Sugerencia)

    def test_cada_medio_tiene_su_plan(self):
        pedido = Pedido(destino='Calle 1')
        for nombre in ('camioneta', 'motocicleta', 'bicicleta', 'dron'):
            with self.subTest(nombre=nombre):
                plan = crear_medio(nombre).planear(pedido, {})
                self.assertEqual(plan.medio, nombre)
                self.assertGreater(plan.horas_estimadas, 0)

    def test_servicio_guarda_plan_y_seguimiento_lo_muestra(self):
        pedido = registrar_pedido('Calle 1', proveedor='xml')
        self.assertEqual(pedido.medio, 'bicicleta')
        respuesta = self.client.get(f'/pedidos/{pedido.id}/')
        self.assertContains(respuesta, 'bicicleta')

    def test_medio_desconocido_no_se_acepta(self):
        with self.assertRaises(ValueError):
            crear_medio('helicóptero')
        self.assertEqual(Pedido.objects.count(), 0)
