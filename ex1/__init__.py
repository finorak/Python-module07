from .Deck import Deck
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard

__all__ = ["Deck", "ArtifactCard", "SpellCard"]


def __getattr__(name: str):
    raise AttributeError(
            f"AttributeError - {name} is not defiened"
            )
