from typing import Any, Union
try:
    from ex0.Card import Card
    from ex2.Combatable import Combatable
    from ex2.Magical import Magical
except Exception as e:
    print(e)


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.combatable = ['attack', 'defend', 'get_combat_stats']
        self.card = ['play', 'get_card_info', 'is_playable']
        self.magical = ['cast_spell', 'channel_mana', 'get_magic_stats']
        self.health_bar = 5
        self.attack_bar = 5
        self.mana = 8
        self.attack_type = attack_type

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

    def get_card_info(self) -> dict:
        card_info: dict[str, Any] = {}
        return card_info

    def is_playable(self, available_mana: int) -> bool:
        try:
            if available_mana < 0:
                return False
            return True
        except Exception as e:
            print(e)
            return False

    def cast_spell(self, spell_name: str,
                   targets: list[str]) -> dict:
        if not self.is_playable(self.mana):
            return {}
        temp = self.mana
        self.mana -= 4
        value = self.mana
        if value < 0:
            return {}
        spell_info: dict[str, Any] = {}
        spell_info['caster'] = self.name
        spell_info['spell'] = spell_name
        spell_info['targets'] = targets
        spell_info['mana_used'] = temp - self.mana
        return spell_info

    def channel_mana(self, amount: int) -> dict:
        info: dict[str, Any] = {}
        try:
            self.mana += amount
            info['channeled'] = amount
            info['total_mana'] = self.mana
            return info
        except Exception as e:
            print(e)
        return info

    def get_magic_stats(self) -> dict:
        stats: dict[str, Any] = {}
        return stats

    def attack(self, target: str) -> dict:
        attack_info: dict[str, Any] = {}
        attack_info['attacker'] = self.name
        attack_info['target'] = target
        attack_info['damage'] = self.attack_bar
        attack_info['combat_type'] = self.attack_type
        return attack_info

    def defend(self, incoming_damage: int) -> dict:
        self.health_bar -= incoming_damage
        value = self.attack_bar - incoming_damage
        if value < 0:
            value = -value
        defense_info: dict[str, Any] = {}
        defense_info['defender'] = self.name
        defense_info['damage_taken'] = incoming_damage
        defense_info['damage_blocked'] = value
        defense_info['still_alive'] = self.health_bar > 0
        return defense_info

    def get_combat_stats(self) -> dict:
        combat_stats: dict[str, Any] = {}
        combat_stats['attacker'] = self.name
        combat_stats['defender'] = self.name
        combat_stats['total_mana'] = self.mana
        combat_stats['health'] = self.health_bar
        combat_stats['attack'] = self.attack_bar
        return combat_stats
