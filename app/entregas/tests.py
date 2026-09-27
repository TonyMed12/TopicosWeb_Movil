from django.test import TestCase

from .models import Pedido


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
