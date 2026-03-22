from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 health: int, attack: int) -> None:
        super().__init__(name, cost, rarity)
        self.health = health
        self.attack = attack
        self.type = "Creature"
        self.mana = 6
        self.playable = True

    def play(self, game_state: dict) -> dict:
        play_result = {}
        mana_temp = self.mana
        print(f"Playing {self.name} with {self.mana} mana available:")
        if not self.is_playable(self.attack):
            self.playable = False
        else:
            self.mana -= 5
        print("Playable", self.playable)
        play_result['card_played'] = self.name
        play_result['mana_used'] = mana_temp - self.mana
        play_result['effect'] = "Creature summoned to battlefield"
        return play_result

    def attack_target(self, target: str) -> None:
        pass

    def get_card_info(self) -> dict:
        creature_info = {}
        creature_info['name'] = self.name
        creature_info['cost'] = self.cost
        creature_info['rarity'] = self.rarity
        creature_info['type'] = self.type
        creature_info['attack'] = self.attack
        creature_info['health'] = self.health
        return creature_info

    

