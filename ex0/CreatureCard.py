from typing import Any, Union
from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str | Any, cost: int, rarity: str,
                 health: int, attack: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.health = health
        self.attack = attack
        self.type = "Creature"
        self.mana = 6
        self.effect = effect
        self.playable = True

    def play(self, game_state: dict) -> dict:
        play_result: dict[str, Union[str, int]] = {}
        mana_temp = self.mana
        if not self.is_playable(self.mana):
            self.playable = False
            print("Playable", self.playable)
            return {}
        self.mana -= 5
        print("Playable", self.playable)
        play_result['card_played'] = self.name
        play_result['mana_used'] = mana_temp - self.mana
        play_result['effect'] = "Creature summoned to battlefield"
        return play_result

    def attack_target(self, target: str) -> None:
        result: dict[str, Union[str, bool, int]] = {}
        result['attacker'] = self.name
        result['target'] = target
        result['damage_dealt'] = 7
        result['combat_resolved'] = True
        print(f"{self.name} attacks {target}:")
        print(f"Attack result: {result}")

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
        creature_info['type'] = self.type
        creature_info['attack'] = self.attack
        creature_info['health'] = self.health
        return creature_info
