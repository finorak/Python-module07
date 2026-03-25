from abc import ABC, abstractmethod


class Magical(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def cast_spell(self, spell_name: str,
                   targets: list) -> dict:
        ...

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        ...

    @abstractmethod
    def get_magic_stats(self) -> dict:
        ...
