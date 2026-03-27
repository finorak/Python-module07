from typing import Any, Union
from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str | Any, cost: int,
                 rarity: str, effect: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.effect = effect
        self.mana = 6
        self.playable = True
        self.type = "Artifact"

    def play(self, game_state: dict) -> dict:
        try:
            result: dict[str, Union[str, int]] = {}
            if not self.is_playable(self.mana):
                self.playable = False
                print("Playable", self.playable)
                return {}
            print("Playable", self.playable)
            self.mana -= 5
            result['card_played'] = self.name
            result['mana_used'] = self.cost
            result['effect'] = self.effect
            return result
        except Exception as e:
            print(e)
            return {}

    def activate_ability(self) -> dict:
        activity: dict[str, Any] = {}
        return activity

    def is_playable(self, available_mana: int) -> bool:
        try:
            if available_mana - 5 < 0:
                return False
            return True
        except Exception as e:
            print(e)
            return False

    def get_card_info(self) -> dict:
        creature_info: dict[str, Union[str, int]] = {}
        creature_info['name'] = self.name
        creature_info['cost'] = self.cost
        creature_info['rarity'] = self.rarity
        return creature_info
