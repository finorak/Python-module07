from typing import Any, Union
from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str | Any, cost: int,
                 rarity: str, effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.used = False
        self.mana = 5
        self.type = "Spell"
        self.durability = 1

    def play(self, game_state: dict) -> dict:
        if self.durability == 0:
            print("Card already played")
            return {}
        try:
            print("Playable", self.is_playable(self.mana))
            self.durability -= 1
            self.result: dict[str, Union[str, int]] = {}
            self.result['card_played'] = self.name
            self.result['mana_used'] = self.cost
            self.result['effect'] = self.effect_type
            return self.result
        except Exception as e:
            print(e)
            return {}

    def activate_ability(self) -> dict:
        ability: dict[str, Any] = {}
        return ability

    def is_playable(self, available_mana: int) -> bool:
        try:
            if available_mana - 5 < 0:
                return False
            return True
        except Exception as e:
            print(e)
            return False

    def get_card_info(self) -> dict:
        creature_info: dict[str, Any] = {}
        creature_info['name'] = self.name
        creature_info['cost'] = self.cost
        creature_info['rarity'] = self.rarity
        return creature_info

    def resolve_effect(self, target: str) -> dict:
        effect_info: dict[str, Any] = {}
        return effect_info
