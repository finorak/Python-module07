from typing import Any
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        play_stats: dict[str, Any] = {}
        return play_stats

    def get_card_info(self) -> dict:
        card_info: dict[str, Any] = {}
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        return True

    def cast_spell(self, spell_name: str,
                   target: list) -> dict:
        spell_info: dict[str, Any] = {}
        return spell_info

    def channel_mana(self, amount: int) -> dict:
        info: dict[str, Any] = {}
        return info

    def get_magic_stats(self) -> dict:
        stats: dict[str, Any] = {}
        return stats

    def attack(self, target: list) -> dict:
        attack_info: dict[str, Any] = {}
        return attack_info

    def defend(self, incoming_damage: int) -> dict:
        defent_info: dict[str, Any] = {}
        return defent_info

    def get_combat_stats(self) -> dict:
        combat_stats: dict[str, Any] = {}
        return combat_stats
