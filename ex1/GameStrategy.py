from abc import ABC
from typing import Any


class GameStrategy(ABC):
    def __init__(self) -> None:
        super().__init__()

    def execute_turn(self, hand: list,
                     battlefield: list) -> dict:
        turn_dict: dict[str, Any] = {}
        return turn_dict

    def get_strategy_name(self) -> str:
        strategy_name = ""
        return strategy_name

    def prioritize_targets(self,
                           available_targets: list[str]) -> list:
        targets: list[str] = []
        return targets
