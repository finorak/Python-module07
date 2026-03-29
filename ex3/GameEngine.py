from typing import Any


class GameEngine:
    def __init__(self) -> None:
        self.turn_simulated = 0
        self.strategy_used: str = ""
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: Any, strategy: Any) -> Any:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Any:
        self.turn_simulated += 1

    def get_engine_status(self) -> Any:
        status: dict[str, int] = {}
        status['turn_simulated'] = self.turn_simulated
        try:
            status['strategy_used'] = self.strategy.__class__.__name__
        except Exception as e:
            print(e)
        status['total_damage'] = self.total_damage
        status['cards_created'] = self.factory.cards_count
        return status
