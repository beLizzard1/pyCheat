# Import the various classes and enumerated types from the deckAndCards.py file
from deckAndCards import Suit, Rank, Card, Deck
from collections import deque
import random

class Hand(Deck):
    def __init__(self, maxLength = 52):
        self.deck = deque(maxlen=maxLength)
    def addSingleCardToHand(self, card):
        self.deck.append(card)
        
class Pile(Deck):

    def populateWithFrenchPlayingDeck(self):
        for a in Suit:
            for b in Rank:
                self.deck.append(Card(a,b))
    
    
    def drawOne(self):
        card = self.deck.pop()
        return card

    def takeAll(self):
        allCards = list(self.deck)
        self.deck.clear()
        return allCards
    
    def shuffle(self):
        # deques are slow at random access so we need to convert self.deck into a list temporarily
        temporaryList = list(self.deck)
        # Use random.shuffle to shuffle this temporary list
        random.shuffle(temporaryList)
        # Remove all the elements from the existing deck 
        self.deck.clear()
        # Add the shuffled cards back (while retaining the max length that was set at the creation of the deque
        self.deck.extend(temporaryList)