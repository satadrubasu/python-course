from wargame.model import Card
from wargame.model.Deck import Deck
from wargame.model.Player import Player



def prep():
    print("Start of Game")

    # Ready the players
    playerOne = Player("One")
    playerTwo = Player("Two")

    # Ready the deck and shuffle
    theDeck = Deck();
    theDeck.shuffleMe()

    # Split the Deck to players
    for i in range(26):
        playerOne.add_cards(theDeck.deal_one())
        playerTwo.add_cards(theDeck.deal_one())

    # Game_on = True
    round = 0
    game_on = True

    while game_on:
        round +=1
        print(f'Round #{round}')

        if len(playerOne.all_cards) == 0:
            print(f"Player One is out of cards - Player TWO Wins")
            game_on = False
            break

        if len(playerTwo.all_cards) == 0:
            print(f"Player Two is out of cards - Player ONE Wins")
            game_on = False
            break

        ## Start a new Round ##
        playerOneCards = []
        playerOneCards.append(playerOne.remove_one())

        playerTwoCards = []
        playerTwoCards.append(playerTwo.remove_one())

        # 3 situations - [ O > T ] Or [ O < T ] Or [ O == T at war]
        ### while at war

        at_war = True

        while at_war:
            if playerOneCards[-1].value > playerTwoCards[-1].value:
                playerOne.add_cards(playerOneCards)
                playerOne.add_cards(playerTwoCards)
                at_war = False
            elif playerOneCards[-1].value < playerTwoCards[-1].value:
                playerTwo.add_cards(playerOneCards)
                playerTwo.add_cards(playerTwoCards)
                at_war = False

            else:
                print('War!')
                if len(playerOne.all_cards) < 3 :
                    print('Player One unable to declare war')
                    print('Player Two wins !!!')
                    game_on = False
                    break
                elif len(playerTwo.all_cards) < 3 :
                    print('Player Two unable to declare war')
                    print('Player One wins !!!')
                    game_on = False
                    break
                else:
                    for num in range(3):
                        playerOneCards.append(playerOne.remove_one())
                        playerTwoCards.append(playerTwo.remove_one())



if __name__== '__main__':
    prep()