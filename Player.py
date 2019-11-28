from HandAndPile import Hand, Pile
from deckAndCards import Rank, Suit
import random
import socket

class Player():
    def __init__(self, playerID):
        # Create unique instances of the variables for this player
        self.playerID = playerID
        self.hand = Hand()
        self.ledger = []
        
    def recieveSingleCard(self, card):
        self.hand.addSingleCardToHand(card)
    
    def addToHand(self, cards):
        self.hand.addToHand(cards):

    def __repr__(self):
        statusString = "Player {} has {} cards in their hand. ".format(self.playerID, len(self.hand))
        cardString = ""
        for card in self.hand.deck:
            cardString += repr(card)      
        return statusString + cardString     

    def makeTransaction(self):
        claim = []
        cardsFromHand = []
        
        return claim, cardsFromHand
        
    def dispute(self, currentPlayer, claim):
        
        
        return False
    
    
    
class TCPPlayer(Player):
    def __init__(self, portNumber):
        super().__init__(self)
        # Now init a whole bunch of TCP related things @Eduardo Henrique, bind to localhost with port
        # Wait for connections from humanPlayers/bots and report the state of the Player instance here that it is connected to.