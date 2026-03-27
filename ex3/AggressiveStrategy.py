from typing import Any


class AgressiveStrategy:
    def __init__(self) -> None:
        pass

    def execute_turn(self, hand: list,
                     battlefield: list) -> dict:
        turn_dict: dict[str, Any] = {}
        return turn_dict

    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    def prioritize_targets(self,
                           available_targets: list) -> list:
        targets: list[str] = []
        return targets
