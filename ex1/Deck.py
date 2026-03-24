import random
from typing import Any
from ex0 import Card


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] | Any = []

    def add_card(self, card: Card) -> None:
        for crd in self.cards:
            if crd.name == card.name:
                return None
        self.cards += [card]

    def remove_card(self, card_name: str) -> bool:
        index = 0
        for card in self.cards:
            if card.name == card_name:
                self.cards.pop(index)
                return True
            index += 1
        return False

    def shuffle(self) -> None:
        self.cards = random.shuffle(self.cards)

    def draw_card(self) -> Card:
        card = random.choice(self.cards)
        return card

    def get_deck_stats(self) -> dict:
        stats: dict[str, Any] = {}
        cards_len = self.ft_len(self.cards)
        if cards_len < 0:
            return stats
        stats['total_cards'] = cards_len
        count_list = self.get_count()
        try:
            stats['creatures'] = count_list['creature_count']
            stats['spells'] = count_list['spell_count']
            stats['artifacts'] = count_list['artifact_count']
            stats['avg_cost'] = f"{self.get_avg_cost():.1f}"
            return stats
        except Exception as e:
            print(e)
            return stats

    def get_count(self) -> dict:
        count_list: dict[str, int] = {}
        for card in self.cards:
            if card.type == 'Creature':
                if 'creature_count' in count_list:
                    count_list['creature_count'] += 1
                else:
                    count_list['creature_count'] = 1
            elif card.type == 'Spell':
                if 'spell_count' in count_list:
                    count_list['spell_count'] += 1
                else:
                    count_list['spell_count'] = 1
            elif card.type == 'Artifact':
                if 'artifact_count' in count_list:
                    count_list['artifact_count'] += 1
                else:
                    count_list['artifact_count'] = 1
        return count_list

    def get_avg_cost(self) -> float:
        costs_lst = [card.cost for card in self.cards]
        cost_sum = 0
        for cost in costs_lst:
            cost_sum += cost
        return cost_sum / self.ft_len(costs_lst)

    def ft_len(self, data: Any) -> int:
        try:
            counter = 0
            for _ in data:
                counter += 1
            return counter
        except Exception as e:
            print(e)
            return -1
