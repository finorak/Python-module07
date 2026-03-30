from typing import Any, Union
from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int,
                 rarity: str, card_id: str,
                 rating: int) -> None:
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.losse = 0
        self.win = 0
        self.rating = rating

    def play(self, game_state: dict) -> dict:
        result: dict[str, Any] = {}
        return result

    def attack(self, target: str) -> dict:
        reports: dict[str, Any] = {}
        return reports

    def get_combat_stats(self) -> dict[str, Any]:
        reports: dict[str, Any] = {}
        return reports

    def get_card_info(self) -> dict[str, Union[str, int, list]]:
        info: dict[str, Union[list, int, str]] = {}
        info['Interfaces'] = [
                cls.__name__ for cls in TournamentCard.__bases__
                ]
        info['Rating'] = self.rating
        info['Record'] = f"{self.losse}-{self.win}"
        return info

    def is_playable(self, available_mana: int) -> bool:
        return True

    def defend(self, incoming_damage: int) -> dict:
        report: dict[str, Any] = {}
        return report

    def calculate_rating(self) -> int:
        return 1

    def get_rank_info(self) -> None:
        pass

    def update_wins(self, wins: int) -> None:
        try:
            self.win += 1
            self.rating += wins
        except Exception as e:
            print(e)

    def update_losses(self, losses: int) -> None:
        try:
            self.losse += 1
            self.rating -= losses
        except Exception as e:
            print(e)

    def get_tournament_stats(self) -> dict[str, Any]:
        stats: dict[str, Any] = {}
        return stats
