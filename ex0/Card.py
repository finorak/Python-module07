from abc import ABC, abstractmethod
from typing import Any, Union


class Card(ABC):
    def __init__(self, name: str, cost: int,
                 rarity: str) -> None:
        super().__init__()
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.type: Union[str, Any] = None

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        ...

    @abstractmethod
    def get_card_info(self) -> dict:
        ...

    @abstractmethod
    def is_playable(self, available_mana: int) -> bool:
        return True
