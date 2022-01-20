# Player adding multiple cards use extend()
# Single card added with append()
# Take out one card pop()
from wargame.model.Card import Card as card


class Player():
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop()

    def add_cards(self,new_cards):
        print(f'adding card - parameter passed -  {type(new_cards)}')
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)

        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

