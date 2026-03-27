from typing import Any
from .CardFactory import CardFactory


class FantasyCardFactory:
    def __init__(self) -> None:
        self.factory: list[Any] = []
        self.card_factory: CardFactory = CardFactory()

    def get_availables_types(self) -> dict[str, list[str]]:
        availables: dict[str, list[str]] = {}
        availables['creatures'] = self.card_factory.creatures
        availables['spells'] = self.card_factory.spells
        availables['artifcats'] = self.card_factory.artifacts
        return availables

    def get_factory_name(self) -> str:
        return self.__class__.__name__
