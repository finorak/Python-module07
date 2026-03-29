from typing import Any


class AgressiveStrategy:
    def __init__(self) -> None:
        pass

    def execute_turn(self, hand: list,
                     battlefield: list) -> dict:
        turn_dict: dict[str, Any] = {}
        turn_dict['card_played'] = hand
        turn_dict['mana_used'] = 5
        turn_dict['targets_attacked'] = battlefield
        turn_dict['damage_dealt'] = 8
        return turn_dict

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self,
                           available_targets: list) -> list:
        if not available_targets:
            return []
        targets: list[str] = [_ for _ in available_targets]
        return targets
