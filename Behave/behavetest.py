import random
import os

class Dealer:

    def __init__(self):
        self.hand = []
    _cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    hand = []

    def _next_card(self):
        return random.choice(self._cards)

    def new_round(self):
        self.hand = [self._next_card(), self._next_card()]

    def _hand_total(self):
        values = [None, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
        value_map = {k: v for k, v in zip(self._cards, values)}

        total = sum([value_map[card] for card in self.hand if card != 'A'])
        ace_count = self.hand.count('A')

        for i in range(ace_count, -1, -1):
            if i == 0:
                total = total + ace_count
            elif total + (i * 11) + (ace_count - i) <= 21:
                total = total + (i * 11) + ace_count - i
                break

        return total

    def get_hand_total(self):
        return self._hand_total()
