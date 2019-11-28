from HandAndPile import Hand, Pile
from deckAndCards import Rank, Suit
import random

class Player():
    hand = Hand()
    
    def __init__(self, playerID):
        self.playerID = playerID

    def recieveSingleCard(self, card):
        self.hand.addSingleCardToHand(card)
        
    def __repr__(self):
        statusString = "Player {} has {} cards in their hand. ".format(self.playerID, len(self.hand))
        cardString = ""
        for card in self.hand.deck:
            cardString += repr(card)      
        return statusString + cardString
        

class gameContainer():
    players = []
    pile = Pile()
    
    def __init__(self, nPlayers):
        # Add players to self.players
        for i in range(nPlayers):
            self.players.append( Player(i) )
        # Add a standard french playing deck to the pile
        self.pile.populateWithFrenchPlayingDeck()
        # Shuffle the pile
        self.pile.shuffle()
        # Distribute cards until not everyone can have the same number
        while( len(self.pile) != 0 ):
            for i in self.players:
                try:
                    i.recieveSingleCard( self.pile.drawOne() )
                except IndexError:
                    break
                    
        # Distribute the remaining cards.
        
        # Select a random rank and set it as the target
        self.currentClaimTarget = random.choice(list(Rank))
        # Initialisation of the game is now done... wooo
    
    