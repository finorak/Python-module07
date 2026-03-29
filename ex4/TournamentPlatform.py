from typing import Union, Any
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.tournament: list[TournamentCard] = []
        self.card_count = 0
        self.match_played = 0
        self.active = "active"

    def register_card(self, card: TournamentCard) -> str:
        if card is None:
            return ""
        try:
            _ = card.name
            self.tournament += [card]
            self.card_count += 1
            return card.name
        except Exception as e:
            return f"{e}"

    def get_card(self, card_id: str) -> TournamentCard | None:
        for card in self.tournament:
            if card.card_id == card_id:
                return card
        return None

    def create_match(self, card1_id: str,
                     card2_id: str) -> dict[str, Union[str, int]]:
        result: dict[str, Union[str, int]] = {}
        result['winner'] = card1_id
        result['loser'] = card2_id
        try:
            card1 = self.get_card(card1_id)
            card2 = self.get_card(card2_id)
            if card1 is None or card2 is None:
                return {}
            if card1.rating > card2.rating:
                winner = card1
                loser = card2
            else:
                winner = card2
                loser = card1
        except Exception as e:
            print(e)
            return {}
        rating = 0
        if winner is not None:
            winner.update_wins(16)
            rating = winner.rating
        result['winner_rating'] = rating
        rating = 0
        if loser is not None:
            loser.update_losses(16)
            rating = loser.rating
        result['loser_rating'] = rating
        self.match_played += 1
        return result

    def get_leaderboard(self) -> list[TournamentCard]:
        board: list[TournamentCard] = self.tournament[:]
        try:
            for i in range(self.ft_len(board)):
                for j in range(self.ft_len(board) - 1):
                    if board[i].rating > board[j].rating:
                        board[i], board[j] = board[j], board[i]
            return board
        except Exception as e:
            print(e)
            return []

    def ft_len(self, lst: Any) -> int:
        counter = 0
        for _ in lst:
            counter += 1
        return counter

    def generate_tournament_report(self) -> dict:
        tournament_report: dict[str, Union[str, int]] = {}
        tournament_report['total_cards'] = self.card_count
        tournament_report['matches_played'] = self.match_played
        tournament_report['avg_rating'] = self.get_avg()
        tournament_report['platform_status'] = self.active
        return tournament_report

    def get_avg(self) -> int:
        counter = 0
        for card in self.tournament:
            try:
                counter += card.rating
            except Exception as e:
                print(e)
                return 0
        if self.card_count == 0:
            return 0
        return counter // self.card_count
