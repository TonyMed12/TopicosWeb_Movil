import json
from dataclasses import dataclass
from xml.etree import ElementTree


@dataclass(frozen=True)
class Sugerencia:
    medio: str
    motivo: str


class AdaptadorJSON:
    def traducir(self, respuesta: str) -> Sugerencia:
        datos = json.loads(respuesta)
        # route_hint y score pertenecen únicamente al formato del proveedor.
        medio = datos['route_hint']
        return Sugerencia(medio=medio, motivo=f"Puntuación simulada: {datos['score']}")


class AdaptadorXML:
    def traducir(self, respuesta: str) -> Sugerencia:
        raiz = ElementTree.fromstring(respuesta)
        medio = raiz.findtext('vehicle')
        if medio is None:
            raise ValueError('La respuesta XML no incluye vehicle')
        return Sugerencia(medio=medio, motivo='Recomendación del proveedor XML simulado')


def proveedor_json_falso(destino: str) -> str:
    """Un proveedor de prueba; no hace ninguna llamada externa."""
    return json.dumps({'route_hint': 'motocicleta', 'score': 0.85})


def proveedor_xml_falso(destino: str) -> str:
    return '<recommendation><vehicle>bicicleta</vehicle></recommendation>'
