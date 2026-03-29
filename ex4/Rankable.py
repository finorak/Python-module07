from abc import ABC, abstractmethod


class Rankable(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def calculate_rating(self) -> int:
        ...

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        ...

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        ...

    @abstractmethod
    def get_rank_info(self) -> None:
        ...
