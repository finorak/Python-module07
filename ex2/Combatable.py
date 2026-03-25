from abc import ABC, abstractmethod


class Combatable(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def attack(self, target: str) -> dict:
        ...

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        ...

    @abstractmethod
    def get_combat_stats(self) -> dict:
        ...
