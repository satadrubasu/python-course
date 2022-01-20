from wargame.resource import Constants as game_constants
from wargame.model.Card import Card
from random import shuffle

class Deck():

 # Instantiate a list of 52 unique cards
 # Shuffle method to shuffle the list.
 # Deal method to pop out a card

    def __init__(self):
        self.all_cards = []
        for suite in game_constants.SUITES:
            for rank in game_constants.RANKS:
                created_card = Card(suite, rank)
                self.all_cards.append(created_card)

    def shuffleMe(self):
        shuffle(self.all_cards)

    def deal_one(self):
        poppedCard = self.all_cards.pop()
        print(f"Deal One - Popped Card : {poppedCard}")
        return poppedCard

    def __str__(self):
        for card in self.all_cards:
            print(f" Card - {card}")

