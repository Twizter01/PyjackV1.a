import random

"""Deck and Card creator"""

class Card:
    def __init__(self, suit: str , number: str) -> None:
        self.suit = suit
        self.number = number


    def card_creator(self, s: str, n: str) -> str:
        card: str = rf"""
            +---------+
            |{s}     {n}|
            |         |
            |         |
            |{n}       {s}|
            +---------+
        """
        return card


def suit_and_number_generator() -> tuple[str, str]:
    number = str(random.randint(2, 10))
    suit = (random.choice(["♤", "♡", "♧", "♢"]))
    return (number, suit)

number, suit = suit_and_number_generator()
card = Card(suit, number=number)
card.card_creator(suit, number)
print(card)