# Player Class
class Player:
    def __init__(
            self,
            bet_total: int,
            total_amount: int,
            moves: list[str] = [],
            cards: list[Card] = [], #type: ignore
            ) -> None:
        self.bet_total = 0 # Starts from zero
        self.total_amount = total_amount
        self.moves = moves
        self.cards = cards

    

