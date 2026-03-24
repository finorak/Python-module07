from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        ...

    def get_card_info(self) -> dict:
        ...

    def is_playable(self, available_mana: int) -> bool:
        return True

    def cast_spell(self, spell_name: str,
                   target: list) -> dict:
        ...

    def channel_mana(self, amount: int) -> dict:
        ...

    def get_magic_stats(self) -> dict:
        ...

    def attack(self, target: list) -> dict:
        ...

    def defend(self, incoming_damage: int) -> dict:
        ...

    def get_combat_stats(self) -> dict:
        ...
