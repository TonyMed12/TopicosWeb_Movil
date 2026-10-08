from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class PlanEntrega:
    medio: str
    horas_estimadas: int
    detalle: str


class MedioDeEntrega(Protocol):
    def planear(self, pedido, contexto) -> PlanEntrega:
        ...


class Camioneta:
    def planear(self, pedido, contexto) -> PlanEntrega:
        return PlanEntrega('camioneta', 4, 'Entrega de mayor capacidad')


class Motocicleta:
    def planear(self, pedido, contexto) -> PlanEntrega:
        return PlanEntrega('motocicleta', 2, 'Entrega urbana')


class Bicicleta:
    def planear(self, pedido, contexto) -> PlanEntrega:
        return PlanEntrega('bicicleta', 3, 'Entrega de proximidad')


class Dron:
    def planear(self, pedido, contexto) -> PlanEntrega:
        return PlanEntrega('dron', 1, 'Entrega aérea simulada')


_MEDIOS = {
    'camioneta': Camioneta,
    'motocicleta': Motocicleta,
    'bicicleta': Bicicleta,
    'dron': Dron,
}


def crear_medio(nombre: str) -> MedioDeEntrega:
    """Fábrica simple: un nombre del dominio selecciona una estrategia."""
    try:
        return _MEDIOS[nombre]()
    except KeyError as error:
        raise ValueError(f'Medio de entrega desconocido: {nombre}') from error
