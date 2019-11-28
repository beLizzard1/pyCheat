from HandAndPile import Hand, Pile
from deckAndCards import Rank, Suit
from Player import Player, TCPPlayer
import random

# class Player():
#     def __init__(self, playerID):
#         # Create unique instances of the variables for this player
#         self.playerID = playerID
#         self.hand = Hand()
        
#     def recieveSingleCard(self, card):
#         self.hand.addSingleCardToHand(card)
        
#     def __repr__(self):
#         statusString = "Player {} has {} cards in their hand. ".format(self.playerID, len(self.hand))
#         cardString = ""
#         for card in self.hand.deck:
#             cardString += repr(card)      
#         return statusString + cardString 
    
# class TCPPlayer(Player):
#     def __init__(self, portNumber):
#         super().__init__(self)
#         # Now init a whole bunch of TCP related things @Eduardo Henrique, bind to localhost with port
#         # Wait for connections from humanPlayers/bots and report the state of the Player instance here that it is connected to.
    

class gameContainer():
    def __init__(self, nPlayers):
        # Create unique instances of the variables for this gameContainer
        self.players = []
        self.pile = Pile()
        # Add players to self.players
        for i in range(nPlayers):
            self.players.append( Player(i) )
        # Add a standard french playing deck to the pile
        self.pile.populateWithFrenchPlayingDeck()
        # Shuffle the pile
        self.pile.shuffle()
        # Distribute cards until no cards remain in the pile
        while( len(self.pile) != 0 ): # Keep on going through the pile until no cards remain
            for i in self.players: # Go through each player iteratively 
                try:
                    i.recieveSingleCard( self.pile.drawOne() ) # Try drawing a card from the pile and giving it to the current player
                except IndexError: # Catch the condition where there are no more cards and break out of the while loop
                    break

        # Select a random rank and set it as the target
        self.currentClaimTarget = random.choice(list(Rank))
        # Initialisation of the game is now done... wooo
    
    