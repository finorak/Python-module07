from .Magical import Magical
from .Combatable import Combatable
from .EliteCard import EliteCard

__all__ = ["Magical", "Combatable", "EliteCard"]


def __getattr__(name: str) -> None:
    raise AttributeError(
            f"AttributeError - {name} not exposed"
            )
