from abc import ABC
from typing import Any
from ex0.Card import Card
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard


class CardFactory(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.creatures: list[Any] | Any = []
        self.spells: list[Any] | Any = []
        self.artifacts: list[Any] | Any = []
        self.cards_count = 0

    def create_creature(self,
                        name_or_power: str | int | None = None
                        ) -> Card:
        creature = CreatureCard(name_or_power, 1, "rare", 2, 5, "melle")
        self.creatures += [creature.name]
        self.cards_count += 1
        return creature

    def create_spell(self,
                     name_or_power: str | int | None = None
                     ) -> Card:
        spell = SpellCard(name_or_power, 1, "rare", "damage")
        self.spells += [spell.name]
        self.cards_count += 1
        return spell

    def create_artifact(self,
                        name_or_power: str | int | None = None
                        ) -> Card:
        artifact = ArtifactCard(name_or_power, 2, "rare", "permanent")
        self.artifacts += [artifact.name]
        self.cards_count += 1
        return artifact

    def create_themed_deck(self, size: int) -> dict:
        themed_deck: dict[str, Any] = {}
        return themed_deck
