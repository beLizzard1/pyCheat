from HandAndPile import Hand, Pile
from deckAndCards import Rank, Suit
from Player import Player, TCPPlayer
import random

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
        # Create a claim ledger
        self.claimLedger = []
        # Initialisation of the game is now done... wooo
        
        
    def startGame(self):
        
        victory = False
        while(true):
            for i in self.players:
                claim, actualCards = i.makeTransaction(self.currentClaimTarget) # It's the first players go. makeTransaction returns both the actual cards being presented and the claim itself.
                
                # Now ask all players if they dispute it?
                for j in self.players:
                    if i == j: # Skip ourselves (that makes no sense)
                        continue
                    else:
                        if( j.dispute(i.playerID, claim) == True ): # If dispute is True then we need to verify the claim against the actualCards
                            if(claim == actualCards):
                                j.addToHand( self.pile.takeAll() ) # They were being truthful the disputer takes all the cards from the Pile
                            else:
                                i.addToHand( self.pile.takeAll() ) # They were caught lying take all the cards from the Pile
                # Now that we've checked all the disputes, we add the claim to the claimLedger
                self.claimLedger.append(claim)
                # Update the currentClaimTarget
                # A claim is a tuple (numberOfCards, Rank) so we need to grab the second entry and update the currentClaimTarget
                self.currentClaimTarget = claim[1]
                # Add the cards to the pile
                self.pile.append(actualCards)                              
                # Has the current player won?
                if( len(i.hand) == 0 ): # Does the player have no cards left in their hand?
                    print("Player {} has Won the game".format(i.playerID))
                    victory = True
                    break
            if(victory == True):
                break
            else:
                continue