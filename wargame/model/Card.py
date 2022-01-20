from wargame.resource import Constants as game_constants
class Card:

    def __init__(self,suite,rank):
        self.suite = suite
        self.rank = rank
        self.value =game_constants.RANK_VALUE[rank]

    def __str__(self):
        return "[" + self.rank + " of " + self.suite + "]"

